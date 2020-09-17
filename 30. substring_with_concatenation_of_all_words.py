import unittest
from typing import List

class Solution:
    # Note that there are several short circuits in various places, so code is difficult to parse.
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Given and input string of concatenated words and a list of words, l, return a list of 
        each index beginning at which all words in l appear the correct number of times with no 
        intervening characters.
        """
        
        # check for actual inputs
        if len(words) == 0 or len(s) == 0:
            return []

        word_length = len(words[0])
        # short circuit if string is too short
        if len(words) > len(s) // word_length:
            return []

        # word_set = set()
        word_dict = {}
        list_of_indices = []

        # Track which words appear and how many times.
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        # As word_dict, but only for the current window.
        window_word_dict = {}
        # This math is annoying. The first window start index is 0, and it iterates by 1, because
        # the start of words in s might not vary by word_length. 
        # The final window starts the number of distinct words * the word length from the end of s.
        for window_start_idx in range(0, len(s) - len(word_dict) * word_length + 1): 
            start_idx = window_start_idx
            window_word_dict = {}
            for this_word_start_idx in range(len(words)):
                cur_idx = window_start_idx + this_word_start_idx * word_length
                # short-circuit
                if s[cur_idx:cur_idx + word_length] not in word_dict:
                    break
                # As above, track each word in the window and they number of appearances of each.
                if s[cur_idx:cur_idx + word_length] in window_word_dict:
                    window_word_dict[s[cur_idx:cur_idx + word_length]] += 1
                else:
                    window_word_dict[s[cur_idx:cur_idx + word_length]] = 1
                if window_word_dict[s[cur_idx:cur_idx + word_length]] > word_dict[s[cur_idx:cur_idx + word_length]]:
                    break
                    
            if window_word_dict == word_dict:
                list_of_indices.append(start_idx)
            
        return list_of_indices


class TestSubstring(unittest.TestCase):

    def test_each_appears_once(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('foobar', ['foo', 'bar']), [0])

    def test_each_appears_multiple(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('foobarfoobarfoobar', ['foo', 'bar']), [0,3,6,9,12])

    def test_each_appears_multiple_not_juxtaposed(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('foobarfoofoobar', ['foo', 'bar']), [0,3,9])

    def test_each_appears_twice_fail(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('foobar', ['foo', 'bar', 'bar']), [])

    def test_each_appears_twice_pass(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('barfoobar', ['foo', 'bar', 'bar']), [0])

    def test_words_start_varying_indices(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('lingmindraboofooowingdingbarrwingmonkeypoundcake', 
                                            ['fooo','barr','wing','ding','wing']), [13])

    def test_empty_sting(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('', ['foo', 'bar', 'bar']), [])

    def test_empty_list(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('barfoo', []), [])

    def test_more_words_than_possible_1(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('barfoo', ['bar', 'foo', 'bar']), [])

    def test_more_words_than_possible_2(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('barfooba', ['bar', 'foo', 'bar']), [])
        

    def test_long_input(self):
        soln = Solution()
        self.assertEqual(soln.findSubstring('a' * 5000, ['a'] * 5001), [])


unittest.main()
