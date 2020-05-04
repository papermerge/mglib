import os
import unittest
from mglib.test.utils import TemporaryNode
from mglib.path import DocumentPath
from mglib.storage import Storage


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MEDIA_ROOT = os.path.join(
    BASE_DIR, "media"
)

class TestStorage(unittest.TestCase):

    def test_delete(self):
        storage = Storage(location=MEDIA_ROOT)

        with TemporaryNode(MEDIA_ROOT) as media_root:
            docs = media_root.add_folder("docs")
            res = media_root.add_folder("results")
            f1 = docs.add_folder("user_1/document_2")
            f1.add_file("doku.pdf")
            res.add_folder("user_1/document_2/pages")

            doc_path = DocumentPath(
                user_id=1,
                document_id=2,
                file_name='doku.pdf'
            )

            self.assertTrue(
                f1.exists()
            )

            storage.delete_document(doc_path)

            self.assertFalse(
                f1.exists()
            )

