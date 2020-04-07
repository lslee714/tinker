from unittest import TestCase

from ..hourglass import hourglass

class TestHourglass(TestCase):

    def test_first_case(self):
        testCase = [
            [1,1,1,0,0,0],
            [0,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,9,2,-4,-4,0],
            [0,0,0,-2,0,0],
            [0,0,-1,-2,-4,0]
        ]
        result = hourglass(testCase)
        self.assertEqual(result, 13)

    def test_second_case(self):
        testCase= [
            [1,1,1,0,0,0],
            [0,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,0,2,4,4,0],
            [0,0,0,2,0,0],
            [0,0,1,2,4,0]
        ]
        result = hourglass(testCase)
        self.assertEqual(result, 19)
