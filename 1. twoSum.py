import unittest

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given list of integers and a target, return list of indices of 
        inputs that add to target. It is guaranteed that a single pair of 
        correct inputs exists.
        """
        already_seen = {}
        for i in range(len(nums)):
            if target - nums[i] in already_seen:
                return [already_seen[target - nums[i]], i]
            already_seen[nums[i]] = i

class Test_two_sum(unittest.TestCase):

    def test_first_and_last(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([1,2,3,6,5], 6), [0,4])

    def test_first_two(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([1,2], 3), [0,1])

    def test_last(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([1,2,3,4,5], 9), [3,4])

    def test_repeated(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([1,2,5,4,5], 10), [2,4])

unittest.main()
