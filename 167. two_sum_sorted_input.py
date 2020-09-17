# remove dupes from sorted array
import unittest
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int):
        """
        Given numbers, a list of sorted ints, and a target int, return the 
        indices of the two values in numbers that add to target. Return
        indices are 1-based.
        """

        ## First version uses dictionaries.
        ## This version is preferred.
        ## O(n) time, but with only one comparison; O(n) space, but actually doubled.
        thus_far = {}
        for idx in range(len(numbers)):
            if target - numbers[idx] in thus_far:
                return thus_far[target-numbers[idx]] + 1, idx + 1
            else:
                thus_far[numbers[idx]] = idx
                
        
        ## Second version uses indices.
        ## Still O(n) time, but with more comparisons; O(n) space, but same, not doubled.
        # idx1 = 0
        # idx2 = len(numbers) - 1
        # while idx1 < idx2:
        #     if numbers[idx1] + numbers[idx2] > target:
        #         idx2 -= 1
        #     elif numbers[idx1] + numbers[idx2] < target:
        #         idx1 += 1
        #     else:
        #         return idx1 + 1, idx2 + 1

        # Need this return with either solution.
        return None


class TestTwoSum(unittest.TestCase):

    def testEmpty(self):
        soln = Solution()
        self.assertIsNone(soln.twoSum([], 9))

    def testSingle(self):
        soln = Solution()
        self.assertIsNone(soln.twoSum([1], 9))

    def testWithNegatives(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([-2,-1,3,5], 4), (2,4))

    def testTheirs1(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([2,7,11,15], 9), (1,2))

    def testTheirs2(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([2,3,4], 6), (1,3))
    
    def testTheirs3(self):
        soln = Solution()
        self.assertEqual(soln.twoSum([-1,0], -1), (1,2))

unittest.main()
