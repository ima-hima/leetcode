import unittest


class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        """Return the longest palindrome in s."""

        # Right now O(n^2), so needs to be improved.
        if len(s) == 0:
            return ''
        longest = s[0]
        max_length = 0
        for i in range(0, len(s)):
            # Is there a way to do this without priming? j starts at -1, so I dunno...
            if self.isPalindrome(s[i:]):
                if len(s[i:]) > max_length:
                    longest = s[i:]
                    break # nothing can be longer, because this ends at the end of s
            for j in range(-1, i-len(s), -1):
                # print('current string', s[i:j])
                if self.isPalindrome(s[i:j]):
                    if len(s[i:j]) > max_length:
                        max_length = len(s[i:j])
                        longest = s[i:j]
                        # print('longest', longest)
                    if i - j < max_length:
                        break

        return longest

    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2 + 1):
            if s[-1-i] != s[i]:
                return False
        return True

class TestLongestPalindrome(unittest.TestCase):

    def test_at_beginning(self):
        soln = Solution()
        self.assertEqual(soln.longestPalindrome('abaa'), 'aba')

    def test_at_end(self):
        soln = Solution()
        self.assertEqual(soln.longestPalindrome('aaba'), 'aba')

    def test_embedded(self):
        soln = Solution()
        self.assertEqual(soln.longestPalindrome('cacaabbaada'), 'aabbaa')

    def test_embedded_with_shorter_at_end(self):
        soln = Solution()
        self.assertEqual(soln.longestPalindrome('deeaabbaadacac'), 'aabbaa')

    def test_entire_string(self):
        soln = Solution()
        self.assertEqual(soln.longestPalindrome('abba'), 'abba')

    def test_is_not_palindrome_even(self):
        soln = Solution()
        self.assertFalse(soln.isPalindrome('abaa'))

    def test_is_not_palindrome_odd(self):
        soln = Solution()
        self.assertFalse(soln.isPalindrome('abacb'))

    def test_is_palindrome_even(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome('abba'))

    def test_is_palindrome_odd(self):
        soln = Solution()
        self.assertTrue(soln.isPalindrome('ababa'))


unittest.main()
