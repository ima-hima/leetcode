import unittest
from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Return whether a number is a palindrome, for instance 123321.
        Negative numbers are false, numbers ending in 0 (divisible by 10)
        are false.
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        ret_val = 0
        input_val = x
        
        while x >= 1:
            ret_val *= 10
            ret_val += x % 10
            if ret_val > 2147483647:
                return 0 
            x //= 10
 
        return input_val == ret_val


class Test_str_str(unittest.TestCase):

    def test_single_digit_odd(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome(1))

    def test_single_digit_even(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome(6))

    def test_single_digit_neg(self):
        soln = Solution()
        self.assertFalse(soln.isPalindrome(-1))

    def test_two_digits(self):
        soln = Solution()
        self.assertFalse(soln.isPalindrome(32))

    def test_zero(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome(0))

    def test_multiple_of_ten(self):
        soln = Solution()
        self.assertFalse(soln.isPalindrome(120))

    def test_not(self):
        soln = Solution()
        self.assertFalse(soln.isPalindrome(123))

    def test_is_even_count(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome(123321))

    def test_is_odd_count(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome(12321))


unittest.main()
