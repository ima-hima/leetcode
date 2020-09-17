import unittest
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ''' 
        Return the number of unique paths from (0,0) to (m,n)
        in an m x n grid, if a path can only go down or right.
        This ended up being, in essense, Needlman-Wunsch.
        '''
        if m == 0 or n == 0:
            return 0
        # initialize m x n grid
        grid = [[[] for y in range(n)] for x in range(m)]
        # Set both 0-axes to values 1, as there is only one
        # path to any of these cells
        for x in range(m):
            grid[x][0] = 1
        for y in range(n):
            grid[0][y] = 1
        # Any cell has as many paths as the cell to its right
        # plus however many paths were available to get to the
        # above cell.
        for x in range(1,m):
            for y in range(1,n):
                grid[x][y] = grid[x-1][y] + grid[x][y-1]
        return grid[m-1][n-1]


class TestThreeSum(unittest.TestCase):

    def test_empty(self):
        soln = Solution()
        self.assertEqual(soln.uniquePaths(0, 7), 0)
        
    def test_simple(self):
        soln = Solution()
        self.assertEqual(soln.uniquePaths(2, 3), 3)

    def test_short(self):
        soln = Solution()
        self.assertEqual(soln.uniquePaths(3, 7), 28)

    def test_inverse_short(self):
        soln = Solution()
        self.assertEqual(soln.uniquePaths(7, 3), 28)

    

unittest.main()
