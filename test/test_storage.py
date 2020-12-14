import os
import unittest
from mglib.test.utils import TemporaryNode
from mglib.path import DocumentPath
from mglib.storage import FileSystemStorage


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MEDIA_ROOT = os.path.join(
    BASE_DIR, "media"
)

class TestStorage(unittest.TestCase):

    def test_delete(self):
        storage = FileSystemStorage(location=MEDIA_ROOT)

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

            storage.delete_doc(doc_path)

            self.assertFalse(
                f1.exists()
            )

    def test_get_versions_1(self):
        storage = FileSystemStorage(location=MEDIA_ROOT)

        with TemporaryNode(MEDIA_ROOT) as media_root:
            docs = media_root.add_folder("docs")
            res = media_root.add_folder("results")
            f1 = docs.add_folder("user_1/document_2")
            f1.add_file("doku.pdf")
            # simulate 2 versions of the document.
            f1.add_folder("v1")
            f1.add_folder("v2")
            res.add_folder("user_1/document_2/pages")

            doc_path = DocumentPath(
                user_id=1,
                document_id=2,
                file_name='doku.pdf',
                version=2
            )
            versions = storage.get_versions(doc_path)

            self.assertEqual(
                versions, [0, 1, 2]
            )

    def test_get_versions_2(self):
        storage = FileSystemStorage(location=MEDIA_ROOT)

        with TemporaryNode(MEDIA_ROOT) as media_root:
            docs = media_root.add_folder("docs")
            f1 = docs.add_folder("user_1/document_2")
            f1.add_file("doku.pdf")

            doc_path = DocumentPath(
                user_id=1,
                document_id=2,
                file_name='doku.pdf',
                version=2
            )
            versions = storage.get_versions(doc_path)

            # document has only one version - the latest
            self.assertEqual(
                versions, [0]
            )

