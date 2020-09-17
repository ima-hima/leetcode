import unittest
from typing import List


first_bad = 0

def isBadVerion(n: int):
    ''' My standin, just for testing. Always returns false if n >= 15. '''
    if n < first_bad:
        return True
    return False

class Solution():
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            # If the first one's bad, they all are.
            return 1

        start = 0
        end = n
        cur_version = n // 2
        while end - start > 1:
            if isBadVersion(start + (end - start // 2)):
                # Very first time, arbitrarily look at left.
                # Every time through, if it's bad, end goes left
                start = start + (end - start // 2)
            else:
                # It's good, start goes right.
                end = start + (end - start // 2)
        if end - start == 0:
            return start
        else:
            return end


class Test_str_str(unittest.TestCase):

    def test_in_middle(self):
        soln = Solution()
        global first_bad
        print(first_bad)
        first_bad = 15
        print(first_bad)

    def test_l_firstbad(self):
        print(first_bad)
        # self.assertTrue(isBadVersion(15))

    
unittest.main()
