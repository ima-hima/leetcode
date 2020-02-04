# longest substring

import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length = 1
        current_start = 0
        already_seen = {} # store what's already occurred and its index
        for i in range(len(s)):
            # It's possible that a character is a repeat but that another character
            # has repeated since. Use the other character's index as a starting point.
            if s[i] in already_seen and already_seen[s[i]] + 1 > current_start:
                current_start = already_seen[s[i]] + 1
            if i - current_start + 1 > length: # Need to add 1 so that we count
                                               # entire substring. I.e. 1 - 0 == 1,
                                               # but length of that substring would be 2.
                length = i - current_start + 1
            already_seen[s[i]] = i
            # print(i, s[i], already_seen[s[i]], current_start, length)
        return length



class Test_length_of_longest(unittest.TestCase):

    def test_all_same(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('aaaaa'), 1)

    def test_empty_string(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring(''), 0)

    def test_ends_at_end(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('abacdefgh'), 8)

    def test_entire_string(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('abcdefghi'), 9)

    def test_length_one(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('a'), 1)

    def test_length_two(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('au'), 2)

    def test_short(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('abcababb'), 3)

    def test_starts_at_beginning(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('abcdefghab'), 8)

    def test_out_of_order_repeats(self): # b repeats first, then a: make sure correct
                                         # index is saved. In this case index of a.
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('abcdefghba'), 8)

    def test_starts_in_middle(self):
        soln = Solution()
        self.assertEqual(soln.lengthOfLongestSubstring('abacdefghba'), 8)

    



unittest.main()
