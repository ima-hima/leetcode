import unittest
from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the order of digits in an integer. 
        That is 123 -> 321. For numbers > 2^32 - 1, return
        2^32 - 1.
        """
        if x == 0:
            return 0
        ret_val = 0
        neg = 1
        if x < 0:
            neg = -1

        x = abs(x)
        while x >= 1:
            ret_val *= 10
            ret_val += x % 10
            if ret_val > 2147483647:
                return 0 
            x //= 10

        return neg * ret_val


class Test_str_str(unittest.TestCase):

    def test_single_digit_odd(self):
        soln = Solution()
        self.assertEqual(soln.reverse(1), 1)

    def test_single_digit_even(self):
        soln = Solution()
        self.assertEqual(soln.reverse(6), 6)

    def test_single_digit_odd_neg(self):
        soln = Solution()
        self.assertEqual(soln.reverse(-1), -1)

    def test_single_digit_even_neg(self):
        soln = Solution()
        self.assertEqual(soln.reverse(-6), -6)

    def test_two_digits(self):
        soln = Solution()
        self.assertEqual(soln.reverse(32), 23)

    def test_zero(self):
        soln = Solution()
        self.assertEqual(soln.reverse(0), 0)

    def test_multiple_of_zero(self):
        soln = Solution()
        self.assertEqual(soln.reverse(120), 21)

    def test_overflow(self):
        soln = Solution()
        self.assertEqual(soln.reverse(799888124156875753), 0)

    def test_overflow_neg(self):
        soln = Solution()
        self.assertEqual(soln.reverse(799888124156875753), 0)

    def test_exactly_two_to_thirty_two(self):
        soln = Solution()
        self.assertEqual(soln.reverse(7463847412), 2147483647)

    def test_exactly_two_to_thirty_two_neg(self):
        soln = Solution()
        self.assertEqual(soln.reverse(-7463847412), -2147483647)

    def test_overflow_by_one(self):
        soln = Solution()
        self.assertEqual(soln.reverse(8463847412), 0)

    def test_overflow_by_one_neg(self):
        soln = Solution()
        self.assertEqual(soln.reverse(-8463847412), 0)
    

unittest.main()
