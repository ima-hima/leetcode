import unittest
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Step through nums, saving sums. For each sum, save tuple of indices.
        """
        sums = {} # This will be a dictionary with key sum and value a set of indices. 
        output_lst = []
        # get all sums, for each sum add indices 
        for first_idx in range(len(nums)):
            for second_idx in range(first_idx+1, len(nums)): # skip first_idx so no doubles
                # for each sum, save indices. This is safe (no doubles)
                # because indices are absolutely ordered.
                this_sum = nums[first_idx] + nums[second_idx]
                sums[this_sum] = sums.get(this_sum, set()).add((first_idx, second_idx))
        # now step through
        for third_idx in range(len(nums)):
            if -nums[third_idx] in sums:
                output_lst.append(sums[-nums[third_idx]].add(nums[third_idx]))
                sums[-nums[third_idx]].add(nums[third_idx])

# get all sums
# for each sum, list all pairs

# for each value in nums, see if opposite is in sums
#     if so
#         for each pair in list sums[value]:
#             if value_idx not in pair:
#                 append

class TestThreeSum(unittest.TestCase):

    def test_single(self):
        soln = Solution()
        

unittest.main()
