import os
import logging
import shutil
from mglib.utils import safe_to_delete

logger = logging.getLogger(__name__)


class Storage:
    """
    Default Storage class which works with DocumentPath and PagePath
    on local host filesystem
    """

    def __init__(self, location=None):
        # by default, this will be something like
        # settings.MEDIA_ROOT
        self._location = location

    @property
    def location(self):
        return self._location

    def abspath(self, _path):
        return os.path.join(
            self.location, _path
        )

    def path(self, _path):
        return self.abspath(_path)

    def delete_document(self, doc_path):
        """
        Receives a mglib.path.DocumentPath instance
        """
        # where original documents and their versions are stored
        abs_dirname_docs = self.path(
            doc_path.dirname_docs
        )
        # where OCRed information and generated thumbnails
        # are stored
        abs_dirname_results = self.path(
            doc_path.dirname_results
        )
        # Before recursively deleting everything in folder
        # double check that there are only
        # .pdf, .txt, .hocr, .jpg files.
        if safe_to_delete(
            abs_dirname_docs
        ):
            shutil.rmtree(abs_dirname_docs)
            if os.path.exists(abs_dirname_docs):
                os.rmdir(abs_dirname_docs)

        if safe_to_delete(
            abs_dirname_results
        ):
            shutil.rmtree(abs_dirname_results)
            if os.path.exists(abs_dirname_results):
                os.rmdir(abs_dirname_results)

    def copy_doc(self, src, dst):
        """
        copy given file src file path to destination
        as absolute doc_path
        """

        dirname = os.path.dirname(
            self.abspath(dst)
        )
        if not os.path.exists(
            dirname
        ):
            os.makedirs(
                dirname, exist_ok=True
            )
        logger.debug(
            f"copy_doc: {src} to {dst}"
        )
        shutil.copyfile(
            src,
            self.abspath(dst)
        )

    def exists(self, _path):
        return os.path.exists(
            self.path(_path)
        )

    def delete_pages(self, doc_path, page_numers):
        """
        Delets pages in the document pointed by doc_path.
        doc_path is an instance of mglib.path.DocumentPath

        In case of success returns document's new version.
        """
        pass

    def reoder_pages(self, doc_path, new_order):
        """
        Reorders pages in the document pointed by doc_path.
        doc_path is an instance of mglib.path.DocumentPath

        In case of success returns document's new version.
        """
        pass

    def paste_pages(
        self,
        dest_doc_path,
        src_doc_path,
        dest_doc_is_new=False,
        after_page_number=False,
        before_page_number=False
    ):
        """
        Pastes pages in the document pointed by dest_doc_path
        from src_doc_path. Both dest and src are instances of
        mglib.path.DocumentPath
        """
        pass


class FileSystemStorage(Storage):
    pass
