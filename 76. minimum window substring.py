import unittest


class Solution:
    def minWindow(self, input_string: str, targets: str) -> str:
        if len(targets) == 0 or len(input_string) < len(targets): 
            return ''

        required_chars = {}
        for t in targets:
            required_chars[t] = required_chars.get(t, 0) + 1

        substring_left = 0
        substring_length = len(input_string) + 1
        window_left = 0
        targets_in_window = 0

        for window_right in range(len(input_string)):
            if input_string[window_right] in required_chars:
                required_chars[input_string[window_right]] -= 1
                if required_chars[input_string[window_right]] >= 0:
                    # I know the char is a target, so add it to count of those in window, as long
                    # as it hasn't gone negative, in which cast it's unnecessary and shouldn't be counted.
                    targets_in_window += 1
                while targets_in_window == len(targets):
                    # Skip if they haven't all been covered yet.
                    if input_string[window_left] in required_chars:
                        if window_right - window_left + 1 < substring_length:
                            substring_left = window_left
                            substring_length = window_right - window_left + 1
                        if input_string[window_left] in required_chars:
                            required_chars[input_string[window_left]] += 1
                            # again, only count if we've cleared one at the end, in which case there's
                            # possibly one less target char inside the window.
                            if required_chars[input_string[window_left]] > 0:
                                targets_in_window -= 1
                    window_left += 1
        # print(input_string[substring_left:substring_left + substring_length], substring_length, len(targets))
        if substring_length > len(input_string):
            # we never caught all of the targets, so left end of substring never moved forward
            return ''
        return input_string[substring_left:substring_left + substring_length]




        

class TestMinWindow(unittest.TestCase):

    def test_cluster_at_front_with_straggler(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('ACOBECZODEBNCAA', 'ABCZ'), 'ACOBECZ')

    def test_first_char_not_in_target(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('DADOBECODEBANC', 'ABC'), 'BANC')

    def test_multiple_copies(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('A', 'AA'), '')

    def test_first_char_not_in_target(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('DDOBECAODEBANMC', 'ABC'), 'BECA')
    
    def test_not_all_there(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('ABDCNNMBANC', 'ABCZ'), '')

    def test_really_short(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('AB', 'A'), 'A')

    def test_repeated_character(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('ADOBECODEBANC', 'AA'), 'ADOBECODEBA')

    def test_their_example(self):
        soln = Solution()
        self.assertEqual(soln.minWindow('ADOBECODEBANC', 'ABC'), 'BANC')

    
    
unittest.main()
