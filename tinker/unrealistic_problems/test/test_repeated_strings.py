from unittest import TestCase

from ..repeated_strings import repeated_strings

class TestRepeatedStrings(TestCase):

    def test_case_1(self):
        testString = 'aba'
        testLength = 10
        result = repeated_strings(testString, testLength)
        self.assertEqual(result, 7)
        
