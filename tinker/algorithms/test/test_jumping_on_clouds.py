from unittest import TestCase

from ..jumping_on_clouds import jumping_on_clouds

class TestJumpingOnClouds(TestCase):

    def test_case_1(self):
        testCase = [0, 0, 1, 0, 0, 1, 0]
        result = jumping_on_clouds(testCase)
        self.assertEqual(result, 4)

    def test_case_2(self):
        testCase = [0, 0, 0, 1, 0, 0]
        result = jumping_on_clouds(testCase)
        self.assertEqual(result, 3)