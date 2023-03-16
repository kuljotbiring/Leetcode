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


# Time complexity is O(n) and memory complexity is O(1) since just pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        # keep going until end of the list
        while curr:
            nxt = curr.next
            # shift pointers
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
