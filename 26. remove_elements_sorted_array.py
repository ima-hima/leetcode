import unittest
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ 
        Remove duplicates from a sorted list in O(n) time and O(1)
        space by swapping items at current end of return list and 
        current item at idx using for loop.
        """
        if len(nums) < 2:
            return 0
        cur_idx = 1
        prev_num = nums[0]
        for idx in range(len(nums)):
            if nums[idx] != prev_num:
                prev_num = nums[idx]
                nums[cur_idx] = nums[idx]
                cur_idx += 1
        return cur_idx

    ############## Accidentally did it twice. First solution is ##############
    ############## better as there are fewer edge cases.        ##############

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     """ 
    #     Remove duplicates from a sorted list in O(n) time and O(1)
    #     space by swapping items at current end of return list and 
    #     current item at idx using while loop
    #     """
        
    #     if len(nums) < 2:
    #         return len(nums)
    #     current_val = nums[0]
    #     idx = 1
    #     swap_location = 1
    #     while idx < len(nums):
    #         while idx < len(nums) and nums[idx] == current_val:
    #             idx += 1
    #         if idx < len(nums):
    #             current_val = nums[idx]
    #             nums[swap_location], nums[idx] = nums[idx], nums[swap_location]
    #             swap_location += 1
    #             idx += 1
    #     # print(nums)
    #     return swap_location



class Test_str_str(unittest.TestCase):

    def test_empty(self):
        soln = Solution()
        input_lst = []
        self.assertEqual(soln.removeDuplicates(input_lst), 0)
        # self.assertEqual(input_lst, [])

    def test_short(self):
        soln = Solution()
        input_lst = [1,1,2]
        self.assertEqual(soln.removeDuplicates(input_lst), 2)
        self.assertEqual(input_lst[:2], [1,2])

    def test_longer(self):
        soln = Solution()
        input_lst = [0,0,1,1,1,2,2,3,3,4]
        self.assertEqual(soln.removeDuplicates(input_lst), 5)
        self.assertEqual(input_lst[:5], [0,1,2,3,4])

    def test_long_repeated(self):
        soln = Solution()
        input_lst = [0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(soln.removeDuplicates(input_lst), 1)
        self.assertEqual(input_lst[:1], [0])

    def test_no_repeats(self):
        soln = Solution()
        input_lst = [0,1,2,3,4,5,6]
        self.assertEqual(soln.removeDuplicates(input_lst), 7)
        self.assertEqual(input_lst[:7], [0,1,2,3,4,5,6])

    def test_skipped_nos(self):
        soln = Solution()
        input_lst = [0,2,3,4,5,5,6]
        self.assertEqual(soln.removeDuplicates(input_lst), 6)
        self.assertEqual(input_lst[:6], [0,2,3,4,5,6])
    

unittest.main()
