# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(-1)
        list_to_iterate = new_list
        while l1 and l2:
            if l1.val < l2.val:
                list_to_iterate.next = l1
                l1 = l1.next
            else:
                list_to_iterate.next = l2
                l2 = l2.next
            list_to_iterate = list_to_iterate.next
            
            
        if l1:
            list_to_iterate.next = l1
        elif l2:
            list_to_iterate.next = l2
            
        return new_list.next
