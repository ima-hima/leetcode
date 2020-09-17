import unittest

class Node:

    def __init__(self, val = None):
        self.value = val
        self.child = Node()



class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        """
        Return the longest common prefix of strings in input list. If there
        is no common prefix return empty list.
        """
        
        if len(strs) == 0:
            return 0

        prefix = Node()
        for char in strs[0]:
            prefix

        # first find shortest word
        # is there a faster way to do this? Like, can we iterate better
        # in second loop?
        try:
            minWordLen = len(strs[0])
        except: # the list is empty
            return ""
        for word in strs[1:]:
            if len(word) < minWordLen:
                minWordLen = len(word)
        
        wordIdx = 0
        strsLen = len(strs)
        stop = False
        while wordIdx < minWordLen and not stop:
            strsIdx = 0
            while strsIdx < strsLen and not stop:
                if strs[strsIdx][wordIdx] != strs[0][wordIdx]:
                    stop = True
                strsIdx += 1
            wordIdx += 1
        if stop:
            return strs[0][:wordIdx - 1]
        return strs[0][:wordIdx]


class Test_two_sum(unittest.TestCase):

    def test_first_and_last(self):
        soln = Solution()
        self.assertEqual(soln.twoSum(["flower","flow","flight"]), ["fl"])

unittest.main()
