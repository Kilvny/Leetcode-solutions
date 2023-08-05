# Certainly! Here's a cleaner solution to reverse a singly-linked list in Python:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head) :
        prv = None
        curr = head 
        while curr: 
            next_node = curr.next # keep track of the next node so we don't lose it
            curr.next = prv # update the next of the current node to be reversed
            prv = curr  # update the prv node to the current node
            curr = next_node # to continue iteratinng
        return prv
        # O(n) time and O(1) space
        
        
        
        """
In this solution, we initialize two pointers, prev and curr, to None and the head of the list, respectively. We then loop through the list, updating the pointers to reverse the list:

next_node stores the next node in the list, so that we don't lose track of it when we update curr.next.
We set curr.next to prev, effectively reversing the direction of the pointer.
We update prev and curr to be the current node and the next node, respectively, so that we can continue iterating through the list.
Finally, we return prev, which is now the head of the reversed list. This solution has a time complexity of O(n) and a space complexity of O(1)."""