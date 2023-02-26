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


