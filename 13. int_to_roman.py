import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        mmm cm xc ix
        

class intToRoman (unittest.TestCase):
    
    def test_empty_input(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi(''), 0)

    def test_all_whitespace(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('    '), 0)

    def test_no_valid_chars(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('abcde'), 0)

    def test_no_leading_valid_chars(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('ab11e'), 0)

    def test_single_digit(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('5'), 5)

    def test_positive(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('11221'), 11221)

    def test_negative(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('-11221'), -11221)

    def test_plus_symbol(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('+11221'), 11221)

    def test_too_large(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('91283472332'), 2147483647)

    def test_too_small(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('-91283472332'), -2147483648)

    def test_internal_neg(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('12-56'), 12)

    def test_leading_whitespace(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('   67'), 67)

    def test_only_hyphen(self):
        soln = Solution()
        self.assertEqual(soln.myAtoi('-'), 0)

unittest.main()
