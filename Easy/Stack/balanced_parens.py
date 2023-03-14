"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # make an empty list to represent stack
        stack = []
        # create a dictionary for key value pairs for closed and open parens
        paren_hash = {")": "(", "]": "[", "}": "{"}

        # iterate through the string
        for paren in s:
            # if the paren is a closing paren
            if paren in paren_hash:
                # if the stack is not empty and the closed paren
                # matches the paren at top if stack
                if stack and stack[-1] == paren_hash[paren]:
                    # remove the paren at top of the stack
                    stack.pop()
                # other-wise tried to add closing paren to empty stack or parens not match
                else:
                    return False
            # current paren was an open paren
            else:
                stack.append(paren)

        # at end if stack is empty return True
        if not stack:
            return True
        # otherwise False
        else:
            return False


