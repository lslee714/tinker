from unittest import TestCase

from ..merge_sort import merge_sort

class test_merge_sort(TestCase):
    """Test cases for the merge_sort_method"""
    def test_already_sorted(self):
        """ALready sorted lists should return the same list"""
        testCase = [1,2,3,4,5]
        result = merge_sort(testCase)
        self.assertEqual(result, testCase)

    def test_empty(self):
        """empty list return empty"""
        testCase = []
        result = merge_sort(testCase)
        self.assertEqual(result, testCase)

    def test_not_sorted(self):
        """An unsorted array should return it sorted ascending"""
        testCase = [3,4,2,1,5]
        result = merge_sort(testCase)
        expected = [1,2,3,4,5]
        self.assertEqual(result, expected)