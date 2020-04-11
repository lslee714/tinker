from unittest import TestCase

from ..list_left_rotation import list_left_rotation

class TestListLeftRotation(TestCase):

    def test_first_case(self):
        testCaseList = [1,2,3,4,5]
        testCaseRotations = 4
        result = list_left_rotation(testCaseList, testCaseRotations)
        self.assertEqual(result, [5,1,2,3,4])

    def test_second_Case(self):
        testCaseList = [41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51]
        testCaseRotations = 10
        result = list_left_rotation(testCaseList, testCaseRotations)
        expected = [77,97,58,1,86,58,26,10,86,51,41,73,89,7,10,1,59,58,84,77]
        self.assertEqual(result, expected)
