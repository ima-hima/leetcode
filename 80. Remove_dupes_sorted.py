# remove dupes from sorted array
import unittest
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ 
        Remove duplicates appearing at most twice from a sorted list 
        in O(n) time and O(n) space.
        """

        # Algorithm: Copy value at current location to the insertion location.
        # Keep track of dupes. On each iteration, copy element to insertion location
        # then advance insertion location, *except* if dupes > 2, in which case 
        # neither advance nor copy, but only increase length of dupes.
        if len(nums) <= 2:
            return len(nums)
        current_val = nums[0]
        insert_location = 0
        dupe_length = 0  # I need to start with 0 dupes in order to catch first element.
        for idx in range(len(nums)):
            if current_val == nums[idx]:
                dupe_length += 1
            else:
                current_val = nums[idx]
                dupe_length = 1
            if dupe_length <= 2:
                nums[insert_location] = nums[idx]
                insert_location += 1

        return insert_location


class TestRemoveDupes(unittest.TestCase):

    # def testEmpty(self):
    #     soln = Solution()
    #     original = []
    #     final = []
    #     length = soln.removeDuplicates(original)
    #     self.assertEqual(final[:length], original)

    # def testSingle(self):
    #     soln = Solution()
    #     original = [1]
    #     final = [1]
    #     length = soln.removeDuplicates(original)
    #     self.assertEqual([1], original[:length])

    # def testNoDupes(self):
    #     soln = Solution()
    #     original = [1,2]
    #     final = [1,2]
    #     length = soln.removeDuplicates(original)
    #     self.assertEqual(final, original[:length])

    def testRepeated(self):
        """ Edge case to make sure idx doesn't go beyond end of list. """
        soln = Solution()
        original = [1,1,1,1]
        final = [1,1]
        length = soln.removeDuplicates(original)
        self.assertEqual(final, original[:length])

    def testSingleRepeat(self):
        """ Edge case to make sure idx doesn't go beyond end of list. """
        soln = Solution()
        original = [1,2,3]
        final = [1,2,3]
        length = soln.removeDuplicates(original)
        self.assertEqual(final, original[:length])

    def testMiddleRepeats(self):
        """ Various repeated, doubled and more, on inside of list. """
        soln = Solution()
        original = [1,2,2,2,3,5,5,5,6,8,8,9]
        final = [1,2,2,3,5,5,6,8,8,9]
        length = soln.removeDuplicates(original)
        self.assertEqual(final, original[:length])

    def testEndRepeats(self):
        """ Repeated at end. """
        soln = Solution()
        original = [1,2,3,5,6,8,9,9,9]
        final = [1,2,3,5,6,8,9,9]
        length = soln.removeDuplicates(original)
        self.assertEqual(final, original[:length])

    def testBeginningRepeats(self):
        """ Repeated >= 2 at beginning of list. """
        soln = Solution()
        original = [1,1,1,2,3,5,6,8,9]
        final = [1,1,2,3,5,6,8,9]
        length = soln.removeDuplicates(original)
        self.assertEqual(final, original[:length])

unittest.main()
