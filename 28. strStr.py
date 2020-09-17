import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for haystack_idx in range(len(haystack) - len(needle) + 1):
            if haystack[haystack_idx] == needle[0]:
                needle_idx = 0
                while haystack_idx < len(haystack) \
                      and needle_idx < len(needle) \
                      and needle[needle_idx] == haystack[haystack_idx]: 
                    needle_idx += 1
                    haystack_idx += 1 # This is safe because loop resets it.
                if needle_idx >= len(needle):
                    return haystack_idx - needle_idx
        return -1


class Test_str_str(unittest.TestCase):

    def test_exists(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', 'll'), 2)

    def test_doesnt_exist(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', 'a'), -1)

    def test_empty_needle(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', ''), 0)

    def test_too_long(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', 'llop'), -1)

    def test_at_beginning(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', 'he'), 0)

    def test_at_end(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', 'llo'), 2)

    def test_incomplete(self):
        soln = Solution()
        self.assertEqual(soln.strStr('hello', 'llp'), -1)

    def test_single_char(self):
        soln =  Solution()
        self.assertEqual(soln.strStr('hello', 'h'), 0)

    def test_repeated_char(self):
        soln =  Solution()
        self.assertEqual(soln.strStr('hhhhhh', 'h'), 0)

    def test_all_but_last_in_needle(self):
        soln =  Solution()
        self.assertEqual(soln.strStr('mississippi', 'issip'), 4)

unittest.main()
