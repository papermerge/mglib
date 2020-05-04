import unittest
from mglib.endpoint import DocumentEp
from mglib.storage import Storage


class TestStep(unittest.TestCase):

    def test_basic(self):
        storage = Storage()

        ep = DocumentEp(
            user_id=1,
            document_id=2,
            file_name='doku.pdf'
        )
        storage.delete(ep)
