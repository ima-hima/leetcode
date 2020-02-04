# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    

    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def appendNode(in_list, curSum):
            # get the remainder and put on new node, 
            # return the new node and the carry value, which 
            # could be > 1
            # advance pointer once on new list
            in_list.next = ListNode(curSum % 10)
            carry = curSum // 10
            return in_list.next, carry

        # don't forget to do mod and remainder on first item in list
        first_node = ListNode((l1.val + l2.val) % 10) # save first_node to return
        cur_node = first_node
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            cur_node, carry = appendNode(cur_node, l1.val + l2.val + carry)
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur_node, carry = appendNode(cur_node, l1.val + carry)
            l1 = l1.next
        while l2:
            cur_node, carry = appendNode(cur_node, l2.val + carry)
            l2 = l2.next
        if carry:
            cur_node.next = ListNode(carry)
            # no need to advance here, as carry is final value
        return first_node
