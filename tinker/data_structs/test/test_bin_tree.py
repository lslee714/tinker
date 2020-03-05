from unittest import TestCase


from ..bin_tree import Node

class test_bin_tree_insert(TestCase):
    def test_one_level(self):
        """Inserting one value should generate put it in the correct spot"""
        testCase = Node(5)

        #insert left
        val = 3
        testCase.insert(val)
        self.assertEqual(testCase.left.val, val)

    def test_two_levels(self):
        """Inserting two values should order and put them in the right spot"""
        testCase = Node(5)

        #insert left twice
        val1 = 3
        val2 = 2

        testCase.insert(val1)
        testCase.insert(val2)

        self.assertEqual(testCase.left.val, val1)
        self.assertEqual(testCase.left.left.val, val2)

    def test_multiple_direction_and_levels(self):
        """Inserting multiple values should order and put them in the right directions and spots"""
        testCase = Node(5)

        # insert left twice
        val1 = 3
        val2 = 2

        testCase.insert(val1)
        testCase.insert(val2)

        #insert right thrice
        val3 = 6
        val4 = 10
        val5 = 7
        testCase.insert(val3)
        testCase.insert(val4)
        testCase.insert(val5)

        self.assertEqual(testCase.left.val, val1)
        self.assertEqual(testCase.left.left.val, val2)
        self.assertEqual(testCase.right.val, val3)
        self.assertEqual(testCase.right.right.val, val4)
        self.assertEqual(testCase.right.right.left.val, val5)

    def test_with_a_lot(self):
        """Should be fast"""
        testCase = Node(5)


class test_bin_tree_search(TestCase):
    def test_in_tree_one_level(self):
        """Inserting one value and searchig for it should return true"""
        testCase = Node(5)

        #insert left
        val = 3
        testCase.insert(val)
        self.assertTrue(testCase.search(3))

    def test_multiple_levels(self):
        """Inserting multiple values and searching for one should be true"""
        testCase = Node(5)

        #insert left twice
        val1 = 3
        val2 = 2

        #insert right thrice
        val3 = 6
        val4= 10
        val5 = 7
        allValues = [val1, val2, val3, val4, val5]
        for val in allValues:
            testCase.insert(val)

        for val in allValues:
            self.assertTrue(val in testCase)

    def test_not_in(self):
        """If tree is set up and value isnt in there, should be false"""
        testCase = Node(5)



        # insert left twice
        val1 = 3
        val2 = 2

        testCase.insert(val1)
        testCase.insert(val2)

        #insert right thrice
        val3 = 6
        val4 = 10
        val5 = 7
        testCase.insert(val3)
        testCase.insert(val4)
        testCase.insert(val5)

        randomValue = 11
        self.assertFalse(testCase.search(randomValue))