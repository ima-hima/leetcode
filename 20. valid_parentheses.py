import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        stack = list()
        parens = {'(': ')', '[': ']', '{': '}'}
        for item in s:
            if item in parens:
                stack.append(item)
            elif len(stack) == 0:
                return False
            elif parens[stack[-1]] != item: # If not it's nested incorrectly.
                return False
            else:
                stack.pop() # They match, remove it from top of the stack.
        if len(stack) == 0:
            return True
        return False



class Test_str_str(unittest.TestCase):

    def test_empty(self):
        soln = Solution()
        self.assertTrue(soln.isValid(""))

    def test_not_nested(self):
        soln = Solution()
        self.assertTrue(soln.isValid("()[]{}"))

    def test_incomplete(self):
        soln = Solution()
        self.assertFalse(soln.isValid("()[]{"))

    def test_incomplete_middle(self):
        soln = Solution()
        self.assertFalse(soln.isValid("()[{}"))

    def test_incorrectly_nested(self):
        soln = Solution()
        self.assertFalse(soln.isValid("([)]"))

    def test_single_closi(self):
        soln = Solution()
        self.assertFalse(soln.isValid("("))
    

unittest.main()
