# remove dupes from sorted array
import unittest
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # I added the following methods for testing purposes.
    def insert(self, val):
        if val == self.val:
            return None
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        else: # it's larger
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)

    def __str__(self):
        return str(self.val)
    # def __str__(self):
    #     retVal = str(self.val) + '\n'
    #     if self.left:
    #         retVal += ' /'
    #     if self.right:
    #         retVal += '\\'
    #     if self.left:
    #         retVal += '\n' + str(self.left)
    #     if self.right:
    #         retVal += '\n' + str(self.right)
    #     return retVal

    # def breadthFirst(self):




class Solution:
    def __init__(self):
        self.vals_thus_far = set()
        self.nodes_not_visited = deque()
    # not_yet_visited = deque()

    def findTarget(self, root: TreeNode, target: int) -> bool:
        """
        Given root, the root of a BST, and target, a target, return True
        if there exist two nodes in root whose values add to target,
        False otherwise.
        """

        # breadth-first search
        if target - root.val in self.vals_thus_far:
            # print('returning True')
            return True

        self.vals_thus_far.add(root.val)
        if root.left:
            self.nodes_not_visited.append(root.left)
        if root.right:
            self.nodes_not_visited.append(root.right)
        if self.nodes_not_visited:
            return self.findTarget(self.nodes_not_visited.popleft(), target)
        
        # Recursion has completed.
        return False
            

class TestTwoSumIV(unittest.TestCase):

    def testEmpty(self):
        soln = Solution()
        soln = Solution()
        root = TreeNode()
        self.assertFalse(soln.findTarget(root, 0))


    def testTheirs1(self):
        soln = Solution()
        root = TreeNode(5)
        for i in [3,6,4,2,7]:
            root.insert(i)
        ans = soln.findTarget(root, 9)
        # print('answer', ans)
        self.assertTrue(ans)

    def testTheirs2(self):
        soln = Solution()
        root = TreeNode(5)
        for i in [3,6,4,2,7]:
            root.insert(i)
        self.assertFalse(soln.findTarget(root, 28))

unittest.main()
