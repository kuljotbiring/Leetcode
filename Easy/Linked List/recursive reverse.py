"""
Given the head of a singly linked list, reverse the list, and return the reversed
list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base case - head is null
        if not head:
            return None

        # maintain new head initially set to head
        new_head = head

        # if there is still a sub-problem - if we can keep reversing
        if head.next:
            new_head = self.reverseList(head.next)
            # since head.next is the next node of head - we want to reverse that link
            # reverse link between head Node and next
            head.next.next = head
        # if head is first Node in list
        head.next = None

        return new_head
