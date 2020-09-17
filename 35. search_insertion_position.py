import unittest
from typing import List

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#     ''' Return insertion point of target in sorted list nums using O(n). '''
#         if len(nums) == 0:
#             return 0
#         idx = 0
#         while idx < len(nums) and nums[idx] < target:
#             idx += 1

#         return idx


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ''' Return insertion point of target in sorted list nums using binary search. '''
        
        # edge cases
        if len(nums) == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        upper_bound = len(nums) - 1
        lower_bound = 0

        while lower_bound < upper_bound:
            idx = lower_bound + (upper_bound - lower_bound) // 2
           
            if target == nums[idx]:
                return idx
            if target == nums[upper_bound]:
                return upper_bound 
            if target == nums[lower_bound]:
                return lower_bound
            if target < nums[idx]:
                upper_bound = idx # Don't subtract 1 because we could get 
                                  # upper_bound == lower_bound and have result 0.
            else: # target > nums[idx]
                  # Add 1 to avoid infinite loop when upper_bound is 
                  # always > lower_bound.
                lower_bound = idx + 1 
        return lower_bound


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
