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

    def path(self, _path):
        return os.path.join(
            self.location, _path
        )

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

    def exists(self, _path):
        return os.path.exists(
            self.path(_path)
        )


class FileSystemStorage(Storage):
    pass
