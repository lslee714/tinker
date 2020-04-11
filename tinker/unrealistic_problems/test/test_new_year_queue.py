from unittest import TestCase

from ..new_year_queue import new_year_queue


class TestNewYearQueue(TestCase):

    def test_case_one(self):
        testCase = [2,1,5,3,4]
        expectedResult = 3
        result = new_year_queue(testCase)
        self.assertEqual(result, expectedResult)
    
    def test_case_two(self):
        testCase = [2,5,1,3,4]
        expectedResult = "Too chaotic"
        result = new_year_queue(testCase)
        self.assertEqual(result ,expectedResult)

    def test_case_three(self):
        testCase = [1,2,5,3,4,7,8,6]
        expectedResult = 4
        result = new_year_queue(testCase)
        self.assertEqual(result, expectedResult)

    def test_case_four(self):
        testCase = [5,1,2,3,7,8,6,4]
        expectedResult = "Too chaotic"
        result = new_year_queue(testCase)
        self.assertEqual(result, expectedResult)

    def test_case_five(self):
        testCase = [1,2,5,3,7,8,6,4]
        expectedResult = 7
        result = new_year_queue(testCase)
        self.assertEqual(result, expectedResult)
