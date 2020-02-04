import unittest

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """ Return median of two sorted arrays. """
        median_position = (len(nums1) + len(nums2)) // 2
        is_even = len(nums1) + len(nums2) % 2 == 0
        idx_nums1 = 0
        idx_nums2 = 0
        i = 0
        sorted_arr = []
        while i < median_position:
            i += 1

            print(median_position, i, idx_nums1, idx_nums2)
            if idx_nums1 >= len(nums1):
                sorted_arr.append(nums2[idx_nums2])
                idx_nums2 += 1
                continue
            if idx_nums2 >= len(nums2):
                sorted_arr.append(nums1[idx_nums1])
                idx_nums1 += 1
                continue
            if nums1[idx_nums1] < nums2[idx_nums2]:
                sorted_arr.append(nums1[idx_nums1])
                idx_nums1 += 1
            elif nums2[idx_nums2] < nums1[idx_nums1]:
                sorted_arr.append(nums2[idx_nums2])
                idx_nums2 += 1
        print('final array:', sorted_arr)
        if is_even:
            return (sorted_arr[-2] + sorted_arr[-1]) / 2
        else:
            return float(sorted_arr[-1])


class Test_Median(unittest.TestCase):

    def test_median_is_one_from_each(self):
        soln = Solution()
        self.assertEqual(soln.findMedianSortedArrays([1,2], [3,4]), 2.5)

unittest.main()
