import unittest

class Solution:
    def trap(self, height) -> int:
        if len(height) == 0:
            return 0

        left_max = {0: height[0]}
        cur_max = height[0]
        for i in range(len(height)):
            if height[i] > cur_max:
                cur_max = height[i]
            left_max[i] = cur_max

        right_max = {len(height) - 1: height[-1]}
        cur_max = height[-1]
        for i in range(len(height) - 1, 0, -1):
            if height[i] > cur_max:
                cur_max = height[i]
            right_max[i] = cur_max

        total = 0
        for i in range(len(height)):
            if height[i] < left_max[i] and height[i] < right_max[i]:
                if left_max[i] > right_max[i]:
                    total += right_max[i] - height[i]
                else:
                    total += left_max[i] - height[i]
        return total


class TestRainwater(unittest.TestCase):

    def test_all_equal(self):
        soln = Solution()
        self.assertEqual(soln.trap([5,5,5,5]), 0)

    def test_bump(self):
        soln = Solution()
        self.assertEqual(soln.trap([1,2,5,4,1]), 0)

    def test_ditch(self):
        soln = Solution()
        self.assertEqual(soln.trap([5,2,1,4,6]), 8)

    def test_empty(self):
        soln = Solution()
        self.assertEqual(soln.trap([]), 0)

    def test_gradient_left(self):
        soln = Solution()
        self.assertEqual(soln.trap([1,2,3,4]), 0)

    def test_gradient_right(self):
        soln = Solution()
        self.assertEqual(soln.trap([4,3,2,1]), 0)

    def test_varying_heights(self):
        soln = Solution()
        self.assertEqual(soln.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

unittest.main()
