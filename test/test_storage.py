import unittest
from mglib.path import DocumentPath
from mglib.storage import Storage


class TestStep(unittest.TestCase):

    def test_basic(self):
        storage = Storage()

        docp = DocumentPath(
            user_id=1,
            document_id=2,
            file_name='doku.pdf'
        )
        storage.delete_document(docp)
