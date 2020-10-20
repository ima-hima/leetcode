import unittest
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return, as a list of lists, all tuples of three numbers that add to 0. 
        There should not be duplicate tuples.

        Use non-Python, i.e. non-dictionary standard 2-sum O(n) time, O(1) space solution: 
        Start with indices at start and end, if less than 0 move start index, if greater
        move end index. For 3-sum do same, but for each position, so O(n^2).
        """

        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        all_triplets = set()
        for current_idx in range(len(nums)):
            start_idx = 0
            end_idx = len(nums) - 1
            while start_idx < current_idx and end_idx > current_idx: 
                if nums[start_idx] > 0 or nums[end_idx] < 0:
                    break
                if nums[start_idx] + nums[end_idx] < -nums[current_idx]:
                    start_idx += 1
                elif nums[start_idx] + nums[end_idx] > -nums[current_idx]:
                    end_idx -= 1
                else: 
                    lookup = tuple(sorted([nums[start_idx], nums[current_idx], nums[end_idx]]))
                    if lookup not in all_triplets:
                        all_triplets.add(lookup)
                    start_idx += 1
                    end_idx -= 1
        return [list(i) for i in all_triplets]


class TestThreeSum(unittest.TestCase):

    def test_their_example(self):
        soln = Solution()
        input_lst = [-1,0,1,2,-1,-4]
        output_lst = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    def test_single(self):
        soln = Solution()
        input_lst = [0]
        output_lst = []
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    def test_empty(self):
        soln = Solution()
        input_lst = []
        output_lst = []
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    def test_all_zeroes(self):
        soln = Solution()
        input_lst = [0,0,0,0]
        output_lst = [[0,0,0]]
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    def test_repeats_in_solutions(self):
        soln = Solution()
        input_lst = [-1,-1,-1,0,2,2,2]
        output_lst = [[-1,-1,2]]
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    # following are test cases that failed
    def test_nested(self):
        soln = Solution()
        input_lst = [3,0,-2,-1,1,2]
        output_lst = [[-2,-1,3],[-2,0,2],[-1,0,1]]
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    def test_nested_perfectly_balanced(self):
        soln = Solution()
        input_lst = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
        output_lst = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)

    def test_unbalanced(self):
        soln = Solution()
        input_lst = [-2,0,1,1,2]
        output_lst = [[-2,0,2],[-2,1,1]]
        self.assertEqual(sorted(soln.threeSum(input_lst)), output_lst)
        


unittest.main()
