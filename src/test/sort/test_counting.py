import unittest
from implex.sort import counting

class TestCountingSort(unittest.TestCase):

    def test_sort_descending_elements(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr = counting.sort(arr)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted_arr, expected)

    def test_sort_random_elements(self):
        arr = [3, 6, 2, 7, 5, 8, 1, 10, 9, 4]
        sorted_arr = counting.sort(arr)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted_arr, expected)

    def test_sort_with_duplicates(self):
        arr = [4, 2, 2, 5, 3, 1, 4, 2, 3]
        sorted_arr = counting.sort(arr)
        expected = [1, 2, 2, 2, 3, 3, 4, 4, 5]
        self.assertEqual(sorted_arr, expected)

    def test_sort_empty_list(self):
        arr = []
        sorted_arr = counting.sort(arr)
        expected = []
        self.assertEqual(sorted_arr, expected)

    def test_sort_single_element(self):
        arr = [42]
        sorted_arr = counting.sort(arr)
        expected = [42]
        self.assertEqual(sorted_arr, expected)

    def test_sort_with_negative_elements(self):
        arr = [-5, -10, 0, -3, 8, 5, -1, 10]
        sorted_arr = counting.sort(arr)
        expected = [-10, -5, -3, -1, 0, 5, 8, 10]
        self.assertEqual(sorted_arr, expected)

if __name__ == "__main__":
    unittest.main()
