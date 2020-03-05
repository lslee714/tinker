from unittest import TestCase

from ..fib_seq import fib

class test_fib(TestCase):
    def test_at_0_and_1(self):
        """First two position should just return first two"""
        testCases =  [0,1]
        evaluated = {}
        for case in testCases:
            self.assertEqual(fib(case, evaluated), case)

    def test_at_further_ahead(self):
        """AFter first two positions, should return corresponding value"""
        testCase = 6
        testCase2 = 8
        #0,1,2,3,5,8,13,21,34
        #fib value of 6 = 8
        #fib value of 8 = 21
        evaluated = {}
        self.assertEqual(fib(testCase, evaluated), 8)
        self.assertEqual(fib(testCase2, evaluated), 21)

    def test_at_really_far(self):
        """Hopefully is faster but same case as further_ahead"""
        testCase = 100
        expectedResult = 354224848179261915075
        evaluated = {}
        self.assertEqual(fib(testCase, evaluated), expectedResult)