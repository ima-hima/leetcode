import unittest
from typing import List

class Solution:
    def __init__(self):
        self.already_visited = {} # list of all points in grid that have been visited
        self.island_count = 0     # total number of islands visited

    def enumerate_island(self, x, y):
        """
        Mark (x, y) as visited. Check all surrounding spaces and recursively call
        if any of those spaces are parts of the same island. At end of calls all
        land attached to (x, y) is visited.
        """
        self.already_visited[(x,y)] = self.grid[x][y]
        
        if x - 1 >= 0 and (x-1, y) not in self.already_visited:
            self.already_visited[(x-1,y)] = self.grid[x-1][y]
            if self.grid[x-1][y] == '1':
                self.enumerate_island(x-1, y)
        if x + 1 < len(self.grid) and (x+1,y) not in self.already_visited:
            self.already_visited[(x+1, y)] = self.grid[x+1][y]
            if self.grid[x+1][y] == '1':
                self.enumerate_island(x+1, y)
        if y - 1 >= 0 and (x, y-1) not in self.already_visited:
            if self.grid[x][y-1] == '1':
                self.enumerate_island(x, y-1)
            self.already_visited[(x,y-1)] = self.grid[x][y-1]
        if y + 1 < len(self.grid[0]) and (x, y+1) not in self.already_visited:
            if self.grid[x][y+1] == '1':
                self.enumerate_island(x, y+1)
            self.already_visited[(x,y+1)] = self.grid[x][y+1]
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Visit each cell in grid. If cell is visited for first time mark as visited.
        If cell is not visited and is land (i.e. value is '1'), then is new island.
        Return total islands found.
        """
        self.grid = grid
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if (x,y) not in self.already_visited:
                    self.already_visited[(x,y)] = self.grid[x][y]
                    if self.grid[x][y] == '1':
                        self.island_count += 1 # I can do this because any previous
                                               # cell on an island that's been seen
                                               # has been visited in enumerate_island()
                        self.enumerate_island(x, y)
        return self.island_count
                    

class TestSubstring(unittest.TestCase):

    def test_one(self):
        soln = Solution()
        self.assertEqual(soln.numIslands([['1']]), 1)

    def test_two(self):
        soln = Solution()
        self.assertEqual(soln.numIslands([['0', '1'],
                                          ['1', '0']
                                         ]
                                        ), 
                                        2
                        )

    def test_large_one(self):
        soln = Solution()
        self.assertEqual(soln.numIslands([['1', '0'], ['1', '0']]), 1)

    def test_their_example_one(self):
        soln = Solution()
        self.assertEqual(soln.numIslands([['1', '1', '1', '1', '0'],
                                          ['1', '1', '0', '1', '0'],
                                          ['1', '1', '0', '0', '0'],
                                          ['0', '0', '0', '0', '0']
                                         ],
                                        ), 
                                        1
                        )

    def test_their_example_two(self):
        soln = Solution()
        self.assertEqual(soln.numIslands([['1', '1', '0', '0', '0'],
                                          ['1', '1', '0', '0', '0'],
                                          ['0', '0', '1', '0', '0'],
                                          ['0', '0', '0', '1', '1']
                                         ],
                                        ), 
                                        3
                        )

    def test_u_shaped(self):
        """ To be sure that all of a given island is visited in y direction. """
        soln = Solution()
        self.assertEqual(soln.numIslands([['1', '1', '0', '1', '0'],
                                          ['1', '1', '0', '1', '0'],
                                          ['0', '1', '1', '1', '0'],
                                          ['0', '0', '0', '1', '1']
                                         ],
                                        ), 
                                        1
                        )

    def test_u_shaped_two(self):
        """ To be sure that all of a given island is visited in x direction. """
        soln = Solution()
        self.assertEqual(soln.numIslands([['1', '1', '0', '0', '0'],
                                          ['1', '1', '1', '0', '0'],
                                          ['0', '0', '1', '0', '0'],
                                          ['1', '1', '1', '0', '1']
                                         ],
                                        ), 
                                        2
                        )

unittest.main()

