from unittest import TestCase

from ..practice import get_pairs, get_valleys, get_min_jumps, equalizeArray, queensAttack, minimumBribes, min_swaps
from ..practice import find_makeable_words, find_anagram_count, count_triplets, frequency_query, activity_notifications

# class TestGetPairs(TestCase):
#     def test_successful(self):
#         test = [1, 1, 2, 2, 3, 3, 3, 4]  # output should be 3
#         self.assertEqual(get_pairs(test), 3)
#
#
# class TestGetValleys(TestCase):
#     def test_successful(self):
#         test = 'UDDDUDUU' #should be 1
#         self.assertEqual(get_valleys(test), 1)
#
# class TestGetMinJumps(TestCase):
#     def test_successful(self):
#
#         test = [0, 0, 0, 1, 0, 0] #should be 3
#         self.assertEqual(get_min_jumps(test), 3)
#
# class TestEqualizeArray(TestCase):
#     def test_successful(self):
#         testCase=  [3, 3, 2, 1, 3]
#         return self.assertEqual(equalizeArray(testCase), 2)
#
#     def test_another(self):
#         testCase = [
#             24,29,70,43,12,27,29,24,41,12,41,43,24,70,24,100,41,43,43,100,29,70,100,43,41,27,70,70,59,41,24,24,29,43,24,
#            27,70,24,27,70,24,70,27,24,43,27,100,41,12,70,43,70,62,12,59,29,62,41,100,43,43,59,59,70,12,27,43,43,27,27,
#             27,24,43,43,62,43,70,29
#         ]
#         return self.assertEqual(equalizeArray(testCase), 63)
#
# class TestGetQueenMoves(TestCase):
#     def test_successful(self):
#         self.assertEqual(queensAttack(8,0,1,1, []), 21)
#
#         self.assertEqual(queensAttack(4,0,4,4, []), 9)
#
#         self.assertEqual(queensAttack(5,3,4,3, [[5,5], [4,2], [2,3]]), 10)
#


class TestMinimumBribes(TestCase):
    def test_first_test_case(self):
        testCase = [2,5,1,3,4]
        self.assertEqual(minimumBribes(testCase), 'Too chaotic')

    def test_second_test_case(self):
        """1 2 5 3 4 7 8 6"""
        testCase = [1,2,5,3,4,7,8,6]
        self.assertEqual(minimumBribes(testCase), 4)

    def test_third_case(self):
        testCase=  [2, 1, 5, 3, 4]
        self.assertEqual(minimumBribes(testCase), 3)


class test_min_swaps(TestCase):
    def test_first_case(self):
        testCase = [4,3,1,2] #[1,2,3,4]
        self.assertEqual(min_swaps(testCase), 3)


class test_makeable_words(TestCase):
    def test_first_case(self):
        words = ['hi', 'my', 'name', 'is', 'luke', 'lee']
        charset = ['l', 'e', 'e', 'u', 'k']
        expected = ['luke', 'lee']
        notExpected = set(words) - set(expected)
        result = find_makeable_words(words, charset)
        for expectedWord in expected:
            self.assertIn(expectedWord, result)

        for word in notExpected:
            self.assertNotIn(word, result)

class test_anagram_count(TestCase):
    def test_first_case(self):
        testCase = 'ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'
        self.assertEqual(find_anagram_count(testCase), 399)

class test_count_triplets(TestCase):
    def test_first_case(self):
        testCase = [1, 2, 1,3, 2, 4]
        multiplier = 2
        self.assertEqual(count_triplets(testCase, multiplier), 3)
    #
    # def test_another_case(self):
    #     testCase = [1, 3, 9, 9, 27, 81]
    #     multiplier = 3
    #     self.assertEqual(count_triplets(testCase, multiplier), 6)

class test_frequency_query(TestCase):
    def test_first_case(self):
        testCase = [(1,5), (1,6), (3,2), (1,10), (1,10), (1,6), (2,5), (3,2)]
        self.assertEqual(frequency_query(testCase), [0,1])

    def test_second_case(self):
        testCase = [(1,3), (2,3), (3,2), (1,4), (1,5), (1,5), (1,4), (3,2), (2,4), (3,2)]
        self.assertEqual(frequency_query(testCase), [0,1,1])

class test_notifications(TestCase):
    def test_first_case(self):
        daysLeadingUp = [2,3,4,2,3,6,8,4,5]
        daysToCheck = 5
        self.assertEqual(activity_notifications(daysLeadingUp, daysToCheck), 2)

    def test_second_case(self):
        daysLeadingUp = [10,20,30,40,50]
        daysToCheck = 3
        self.assertEqual(activity_notifications(daysLeadingUp, daysToCheck), 1)