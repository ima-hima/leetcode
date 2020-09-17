import unittest
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        idx = 0
        while idx < len(nums) and nums[idx] < target:
            idx += 1
        return idx

class Test_str_str(unittest.TestCase):

    def test_in_middle(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,2,3,4], 3), 2)

    def test_at_beginning(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,2,3,4], 1), 0)

    def test_at_end(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,2,3,4], 4), 3)

    def test_missing_from_end(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,2,3,4], 5), 4)

    def test_missing_from_middle(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,2,3,6], 5), 3)

    def test_missing_from_beginning(self):
        soln = Solution()
        self.assertEqual(soln.searchInsert([1,2,3,4], 0), 0)


unittest.main()
