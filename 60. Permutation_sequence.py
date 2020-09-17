import unittest
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # build list of length n?
        for left in range(len(n)):
            # reset list
            # n[0] := n[left]
            # item to move := n[len-1]
            for right in range(len(n-1), left, -1):
                # list[]

class TestInsertionPoint(unittest.TestCase):

    def test_empty(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([], 1), 0)

    def test_very_short_input(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([2], 2), 0)
        
    def test_equals_member(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,3,5,6], 5), 2)

    def test_at_beginning(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,3,5,6], 0), 0)

    def test_at_beginning(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,3,5,6], 2), 1)

    def test_after_end(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,3,5,6], 7), 4)

    def test_between_even(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,3], 2), 1)

    def test_between_odd(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,3,5], 4), 2)


unittest.main()
