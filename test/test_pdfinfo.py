import os
import unittest

from mglib.pdfinfo import get_pagecount

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR, "data"
)


def get_filepath(filename):
    return os.path.join(DATA_DIR, filename)


class TestPDFinfo(unittest.TestCase):

    def test_basic_pdf(self):
        page_count = get_pagecount(get_filepath("berlin.pdf"))

        self.assertEqual(
            page_count,
            2
        )

    def test_basic_jpeg(self):
        page_count = get_pagecount(get_filepath("berlin.jpeg"))

        self.assertEqual(
            page_count,
            1
        )

    def test_basic_jpg(self):
        page_count = get_pagecount(get_filepath("berlin.jpg"))

        self.assertEqual(
            page_count,
            1
        )

    def test_basic_png(self):
        page_count = get_pagecount(get_filepath("berlin.png"))

        self.assertEqual(
            page_count,
            1
        )

    def test_basic_tiff(self):
        # in case input file has extention tiff extension
        # it will internally call get_tiff_pagecount method
        page_count = get_pagecount(get_filepath("text.tiff"))

        self.assertEqual(
            page_count,
            2
        )
