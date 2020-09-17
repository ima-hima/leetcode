import unittest
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Modify nums to have the numbers 0, 1, 2 sorted in place.
        Use a one-pass algorithm.
        Do not return anything, modify nums in-place instead.
        This algorithm is O(n), as we look at each index only once.
        """
        
        # First deal with edge cases.
        if len(nums) < 2:
            return
        if len(nums) == 2:
            if nums[0] > nums[1]: # otherwise, already sorted
                nums[0], nums[1] = nums[1], nums[0]
            return

        # Set end_of_zeroes, then end_of_ones if possible.
        end_of_zeroes = 0 
        while end_of_zeroes < len(nums) and nums[end_of_zeroes] == 0:
            end_of_zeroes += 1
        end_of_ones = end_of_zeroes
        # while end_of_ones < len(nums) and nums[end_of_ones] == 1:
        #     end_of_ones += 1
        # At this point, end_of_zeroes is pointing at index after last 0 and
        # end_of_ones at either next element or next element last 1.

        # Step back from end of list, keeping track of end of 0s and 1s. 
        # idx points to either end of list or first 2. When sorting swap value at
        # idx with value at either end_of_ones or end_of_zeroes. 
        idx = len(nums) - 1
        while idx >= end_of_ones:
            if nums[idx] == 2:
                idx -= 1
            elif nums[idx] == 1:
                nums[end_of_ones], nums[idx] = nums[idx], nums[end_of_ones]
                end_of_ones += 1
            else:
                nums[end_of_zeroes], nums[idx] = nums[idx], nums[end_of_zeroes]
                end_of_zeroes += 1
                if end_of_ones < end_of_zeroes:
                # end_of_ones *has* to be > end_of_zeroes
                # We can do this because 0s and 1s are already abutting
                # In this case, there are no 1s yet sorted.
                    end_of_ones = end_of_zeroes
                



class TestSortColors(unittest.TestCase):

    def test_empty(self):
        soln = Solution()
        nums = []
        soln.sortColors(nums)
        self.assertEqual(nums, [])

    def test_single(self):
        soln = Solution()
        nums = [1]
        soln.sortColors(nums)
        self.assertEqual(nums, [1])
        # I'm going to assume if it works for [1] it's also true for [2] and [3].

    def two_sorted(self):
        soln = Solution()
        nums = [0,2]
        soln.sortColors(nums)
        self.assertEqual(nums, [0,2])

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

