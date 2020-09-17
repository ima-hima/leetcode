from typing import List
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        this_node = head
        val_to_insert = this_node.val

        while this_node.next:
            while val < this_node.next.val:
                this_node = this_node.next
            new_node = ListNode(val, this_node)
            head = head.next
            val_to_insert = head.val 


class testInsertionSort(unittest.TestCase):
    
    def test_empty(self):
        to_sort = []
        soln = Solution()
        self.assertEqual(soln.insertionSortList(to_sort), [])



unittest.main()

