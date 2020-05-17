import logging
import shutil
from os import listdir
from os.path import isdir, join

from pmworker.pdftk import make_sure_path_exists
from mglib.path import (DocumentPath, PagePath)
from mglib.step import Steps

"""
OCR operations are per page. Cut/Paste/Delete/Reorder are per page as well.
So it does not make sense to rerun such a heavy operation as OCR again, instead
we can do some magic tricks (copy them from one location to another)
on already extracted txt and hocr files.

OcrMigrate class takes care of this sort of txt/hocr files moves.
"""

logger = logging.getLogger(__name__)


class OcrMigrate:
    """
    Insead of running again OCR operation on changed document AGAIN
    (e.g. after pages 2 and 3 were deleted)
    text files which are result of first (and only!) OCR are moved
    (moved = migrated) inside new version's folder.
    Basically migrate/move files instead of rerunning OCR operation.

    For each affected page (page_x), following files will need to be migrated:
        * <version>/pages/page_x.txt
        * <version>/pages/page_x/50/*.hocr
        * <version>/pages/page_x/75/*.hocr
        * <version>/pages/page_x/100/*.hocr
        * <version>/pages/page_x/125/*.hocr
        from <old_version> to <new_version>

    Which pages are affected depends on the operation.
    """

    def __init__(self, src_ep, dst_ep):
        # Both endpoints shoud be instance of DocumentEp

        for inst in [src_ep, dst_ep]:
            if not isinstance(inst, DocumentEp):
                raise ValueError(
                    "OcrMigrate args must be DocumentEp instances"
                )

        self.src_ep = src_ep
        self.dst_ep = dst_ep

    def migrate_delete(self, deleted_pages):
        page_count = get_pagecount(self.src_ep)
        if len(deleted_pages) > page_count:
            logger.error(
                f"deleted_pages({deleted_pages}) > page_count({page_count})"
            )
            return

        assigns = get_assigns_after_delete(
            total_pages=page_count,
            deleted_pages=deleted_pages
        )
        for a in assigns:
            for step in Steps():
                src_page_ep = PageEp(
                    document_ep=self.src_ep,
                    page_num=a[1],
                    step=step,
                    page_count=page_count
                )
                dst_page_ep = PageEp(
                    document_ep=self.dst_ep,
                    page_num=a[0],
                    step=step,
                    page_count=page_count - len(deleted_pages)
                )
                copy_page(
                    src_page_ep=src_page_ep,
                    dst_page_ep=dst_page_ep
                )
