import unittest


class Solution:
    def myAtoi(self, input_str: str) -> str:
        """
        Take in numerical string. Return corresponding negative or positive int. 
        Remove leading spaces. 
        Empty inputs return 0. Ignore non-numeric characters after first number. 
        Any non-whitespace leading chars return 0. Ignore leading plus (+) symbols.
        """
        if len(input_str) == 0:
            return 0

        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
                  '7': 7, '8': 8, '9': 9
                 }
        idx = 0
        # Strip off leading whitespace
        while idx < len(input_str) and input_str[idx] == ' ':
            idx += 1

        if idx >= len(input_str):
            return 0

        negative = False
        if input_str[idx] == '-':
            negative = True
            idx += 1
        elif input_str[idx] == '+':
            idx += 1

        # At this point if there are any non-numeric chars we'll return 0 by default.
        # Collect numerics into list; step backward through list to generate integer.
        digit_lst = []
        while idx < len(input_str) and input_str[idx] in digits:
            digit_lst.append(digits[input_str[idx]])
            idx += 1
        i = 1
        total = 0
        for idx in range(1, len(digit_lst) + 1):
            total += digit_lst[-idx] * i
            i *= 10
        if negative:
            total = -total
        if total > 2147483647:
            total = 2147483647
        elif total < -2147483648:
            total = -2147483648
        return total
        

class Test_AtoI (unittest.TestCase):
    
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
