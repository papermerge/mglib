import os
import logging

from mglib.runcmd import run

logger = logging.getLogger(__name__)


def convert_tiff2pdf(doc_url):

    logger.debug(f"convert_tiff2pdf for {doc_url}")
    # basename is filename + ext (no path)

    basename = os.path.basename(doc_url)
    base_root, base_ext = os.path.splitext(basename)
    root, ext = os.path.splitext(doc_url)
    new_doc_url = f"{root}.pdf"

    logger.debug(
        f"tiff2pdf source={doc_url} dest={new_doc_url}"
    )

    cmd = (
        "convert",
        doc_url,
        new_doc_url,
    )

    run(cmd)

    # returns new filename
    return f"{base_root}.pdf"
