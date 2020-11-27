import os
import unittest
from unittest import mock
from mglib import pdftk
from mglib.conf import settings
from mglib.runcmd import run

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")


class TestPdfLib(unittest.TestCase):
    def test_ranges_for_reorder(self):
        actual = pdftk.cat_ranges_for_reorder(4, [
            {"page_order": 1, "page_num": 4},
            {"page_order": 2, "page_num": 3},
            {"page_order": 3, "page_num": 2},
            {"page_order": 4, "page_num": 1}
            ])
        expected = [4,3,2,1]
        assert expected == actual

        self.assertRaises(ValueError, pdftk.cat_ranges_for_reorder, 2, [])
        self.assertRaises(KeyError, pdftk.cat_ranges_for_reorder, 2, [
            {"page_order": 3, "page_num": 4},
            {"page_order": 5, "page_num": 6}
            ])

    def test_delete_pages(self):
        input_file = os.path.join(DATA_DIR, "berlin.pdf")
        output_file = os.path.join(DATA_DIR, "berlin2.pdf")

        with mock.patch("mglib.pdftk.run") as run_func:
            pdftk.delete_pages(input_file, output_file, [1])
            run_func.assert_called()
            run_func.assert_called_with(
                [settings.BINARY_PDFTK, input_file, "cat", "2", "output", output_file]
            )

    def test_cat_ranges_for_delete(self):
        page_count = 22
        page_numbers = range(1, 23)

        actual = pdftk.cat_ranges_for_delete(page_count, [21])
        expected = list(page_numbers)
        expected.remove(21)
        assert actual == expected

        actual = pdftk.cat_ranges_for_delete(page_count, [1])
        expected = list(page_numbers)
        expected.remove(1)
        assert actual == expected

        actual = pdftk.cat_ranges_for_delete(page_count, [1, 7, 10])
        expected = list(page_numbers)
        expected.remove(1)
        expected.remove(7)
        expected.remove(10)
        assert actual == expected

        self.assertRaises(ValueError, pdftk.cat_ranges_for_delete, page_count, ["1"])

    def test_split_ranges(self):
        page_count = 9
        page_numbers = list(range(1, 10))

        self.assertRaises(ValueError, pdftk.split_ranges, 9, after="a", before=False)
        self.assertRaises(ValueError, pdftk.split_ranges, 9, after=False, before=True)

        actual1, actual2 = pdftk.split_ranges(page_count, 1, False)
        expected1 = [1]
        expected2 = [2, 3, 4, 5, 6, 7, 8, 9]
        assert actual1 == expected1
        assert actual2 == expected2

        actual1, actual2 = pdftk.split_ranges(page_count, False, 2)
        expected1 = [1]
        expected2 = [2, 3, 4, 5, 6, 7, 8, 9]
        assert actual1 == expected1
        assert actual2 == expected2

        actual1, actual2 = pdftk.split_ranges(page_count)
        expected1 = list(range(1, page_count + 1))
        expected2 = []
        assert actual1 == expected1
        assert actual2 == expected2

    def test_reorder_pages(self):
        input_file = os.path.join(DATA_DIR, "berlin.pdf")
        output_file = os.path.join(DATA_DIR, "berlin2.pdf")
        new_order = [ 
                {'page_num': 2, 'page_order': 1}, 
                {'page_num': 1, 'page_order': 2}, 
                ] 

        with mock.patch("mglib.pdftk.run") as run_func:
            pdftk.reorder_pages(input_file, output_file, new_order)
            run_func.assert_called()
            run_func.assert_called_with(
                [settings.BINARY_PDFTK, input_file, "cat", "2", "1", "output", output_file]
            )

    def test_paste_pages_into_existing_doc(self):
        input_file = os.path.join(DATA_DIR, "berlin.pdf")
        output_file = os.path.join(DATA_DIR, "berlin2.pdf")
        datalist = [] 

        with mock.patch("mglib.pdftk.run") as run_func:
            pdftk.paste_pages_into_existing_doc(input_file, output_file, datalist)
            run_func.assert_called()
            run_func.assert_called_with(
                [settings.BINARY_PDFTK, "A=" + input_file, "cat", "A1", "A2", "output", output_file]
            )

        datalist = [{"src": input_file, "page_nums": "34"}] 

        with mock.patch("mglib.pdftk.run") as run_func:
            pdftk.paste_pages_into_existing_doc(input_file, output_file, datalist, 1)
            run_func.assert_called()
            run_func.assert_called_with(
                [settings.BINARY_PDFTK, "A=" + input_file, "B=" + input_file, "cat", "A1", "B3",
                    "B4", "A2", "output", output_file]
            )
    def test_paste_pages(self):
        input_file = os.path.join(DATA_DIR, "berlin.pdf")
        output_file = os.path.join(DATA_DIR, "berlin2.pdf")
        datalist = [] 

        with mock.patch("mglib.pdftk.run") as run_func:
            pdftk.paste_pages(input_file, output_file, datalist, False)
            run_func.assert_called()
            run_func.assert_called_with(
                [settings.BINARY_PDFTK, "A=" + input_file, "cat", "A1", "A2", "output", output_file]
            )

        datalist = [{"src": input_file, "page_nums": "34"}] 

        with mock.patch("mglib.pdftk.run") as run_func:
            pdftk.paste_pages(input_file, output_file, datalist)
            run_func.assert_called()
            run_func.assert_called_with(
                [settings.BINARY_PDFTK, "A=" + input_file, "cat", "A3", "A4",
                    "output", output_file]
            )
