import unittest
from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        best = -sys.maxsize
        current_total = 0
        for i in range(len(nums)):
            # print(-i)
            current_total = max(nums[i], current_total + nums[i])
            best = max(best, current_total)
            # if totals[i] < totals[location_of_low]:
            #     current_low = nums[i]
            #     location_of_low = i
            # print(current_total, best)

        return best
                


class TestMaximumSubarray(unittest.TestCase):

    def test_empty(self):
        soln = Solution()
        nums = []
        self.assertEqual(soln.maxSubArray(nums), 0)

    def test_single(self):
        soln = Solution()
        nums = [1]
        self.assertEqual(soln.maxSubArray(nums), 1)

    def test_theirs(self):
        soln = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(soln.maxSubArray(nums), 6)

    def two_unsorted(self):
        soln = Solution()
        nums = [2,1]
        soln.sortColors(nums)
        self.assertEqual(nums, [2,1])

    def test_simple(self):
        soln = Solution()
        nums = [0,1,2]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

    def test_grouped(self):
        soln = Solution()
        nums = [0,0,1,1,2,2]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])

    def test_all_one_value(self):
        soln = Solution()
        nums = [1,1,1,1,1]
        soln.sortColors(nums)
        self.assertEqual(nums, [1,1,1,1,1])

    def test_ordered_groups(self):
        soln = Solution()
        nums = [0,1,2,0,1,2,0,1,2,0,1,2]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,0,0,0,1,1,1,1,2,2,2,2])

    def test_sorted_backward_even(self):
        soln = Solution()
        nums = [2,2,1,1,0,0]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])

    def test_sorted_backward_odd(self):
        soln = Solution()
        nums = [2,2,1,1,0]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,1,1,2,2])

    def test_unsorted(self):
        soln = Solution()
        nums = [0,1,0,1,2]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2])

    def test_only_two_values(self):
        soln = Solution()
        nums = [1,2,1,2]
        soln.sortColors(nums)
        self.assertEqual(nums, [1,1,2,2])

    def test_unordered_three(self):
        soln = Solution()
        nums = [0,2,1]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,1,2])


unittest.main()

