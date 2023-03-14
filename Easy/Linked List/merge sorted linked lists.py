"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the
nodes of the first two lists.

Return the head of the merged linked list

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # make dummy node to avoid edge case of inserting into empty list
        dummy = ListNode()
        tail = dummy

        # iterate through the list while they are not empty
        while list1 and list2:
            # check which node is lower and insert into new list & iterate forward
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # iterate forward in new list
            tail = tail.next

        # if any list is remaining append that to end of new list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
