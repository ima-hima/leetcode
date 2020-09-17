import unittest
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        """Return Arabic number of Roman numeral entered as string."""
        ret_val = 0
        nexts = {'I': ['V', 'X'], 'X': ['C', 'L'], 'C': ['D', 'M']}
        values = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 
                  'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 
                  'CM': 900, 'M': 1000}

        idx = 0
        while idx < len(s):
            if s[idx] in nexts and idx + 1 < len(s) and s[idx+1] in nexts[s[idx]]:
                ret_val += values[s[idx:idx+2]]
                idx += 2
            else:
                ret_val += values[s[idx]]
                idx += 1

        return ret_val


class Test_str_str(unittest.TestCase):

    def test_I(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('I'), 1)

    def test_I(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('M'), 1000)

    def test_IV(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('IV'), 4)

    def test_VI(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('VI'), 6)

    def test_IX(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('IX'), 9)

    def test_MCMXVII(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('MCMXVII'), 1917)

    def test_MMMCMXCIX(self):
        soln = Solution()
        self.assertEqual(soln.romanToInt('MMMCMXCIX'), 3999)


unittest.main()
