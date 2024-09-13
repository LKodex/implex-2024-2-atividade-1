import unittest
from implex.sort import counting

@unittest.skip("Not implemented yet!")
class TestCountingSort(unittest.TestCase):

    def test_sort_descending_elements(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        sortedArr = counting.sort(arr)
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEquals(sortedArr, expected)
    
    def test_ordered_elements(self):
        arr = [-3, -2, -1, 0, 1, 2, 3]
        sortedArr = counting.sort(arr)
        expected = [-3, -2, -1, 0, 1, 2, 3]
        self.assertEquals(sortedArr, expected)

    def test_empty_list(self):
        arr = []
        sortedArr = counting.sort(arr)
        expected = []
        self.assertEquals(sortedArr, expected)
    
    def test_one_element(self):
        arr = [0]
        sortedArr = counting.sort(arr)
        expected = [0]
        self.assertEquals(sortedArr, expected)
    
    def test_two_unordered_elements(self):
        arr = [0, -1]
        sortedArr = counting.sort(arr)
        expected = [-1, 0]
        self.assertEquals(sortedArr, expected)
    
    def test_two_ordered_elements(self):
        arr = [0, 1]
        sortedArr = counting.sort(arr)
        expected = [0, 1]
        self.assertEquals(sortedArr, expected)

if __name__ == "__main__":
    unittest.main()
