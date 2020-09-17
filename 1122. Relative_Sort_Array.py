from typing import List
import unittest

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Return sorted arr1. Sorted is defined as sorted by arr2 followed by any
        leftover values in ascending sorted order. All items in arr2 are guaranteed
        to be in arr1.
        """
        arr1_vals = {}
        for val in arr1:
            arr1_vals[val] = arr1_vals.get(val, 0) + 1
        extra_vals = []
        output_sorted = []
        for val in arr2:
            output_sorted += [val] * arr1_vals[val]
            del(arr1_vals[val])
        extra_vals = []
        for key in sorted(list(arr1_vals)):
            extra_vals += arr1_vals[key] * [key]
        output_sorted += extra_vals
        return output_sorted


class Test_sort_array(unittest.TestCase):

    def test_their_example(self):
        soln = Solution()
        self.assertEqual(soln.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]), [2,2,2,1,4,3,3,9,6,7,19])

    def test_short_version(self):
        soln = Solution()
        self.assertEqual(soln.relativeSortArray([2,3,1,3], [1,2,3]), [1,2,3,3])

    def test_empty_list(self):
        soln = Solution()
        self.assertEqual(soln.relativeSortArray([1,3,2], []), [1,2,3])

    def test_multiples_version(self):
        soln = Solution()
        self.assertEqual(soln.relativeSortArray([1,3,1,1,2,3,4,2,3,4,1,5,5,1,2,1,3], [3,4,1,2]), [3,3,3,3,4,4,1,1,1,1,1,1,2,2,2,5,5])

    # def test_repeated(self):
    #     soln = Solution()
    #     self.assertEqual(soln.relativeSortArray([1,2,5,4,5], 10), [2,4])

unittest.main()
