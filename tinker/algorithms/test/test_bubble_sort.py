from unittest import TestCase

from ..bubble_sort import bubble_sort

class test_bubble_sort(TestCase):
    """Test cases for the bubble_sort_method"""
    def test_already_sorted(self):
        """ALready sorted lists should return the same list"""
        testCase = [1,2,3,4,5]
        result = bubble_sort(testCase)
        self.assertEqual(result, testCase)

    def test_not_sorted(self):
        """An unsorted array should return it sorted ascending"""
        testCase = [3,4,2,1,5]
        result = bubble_sort(testCase)
        expected = [1,2,3,4,5]
        self.assertEqual(result, expected)

    def test_another_scenario(self):
        test_case = [1,3,2,1,5,4,32, 3, 1, 8]
        expected = sorted(test_case)
        result = bubble_sort(test_case)
        self.assertEqual(result, expected)