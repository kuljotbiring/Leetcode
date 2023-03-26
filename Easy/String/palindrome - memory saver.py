"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


# Time complexity: O(n). Space complexity O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set up pointers on either end of string
        left = 0
        right = len(s) - 1

        # continue the algorithm while the pointers have not met
        while left < right:
            # skip over non-alphanumeric chars - don't go out of bounds/pass other pointer
            while left < right and not self.alpha_num(s[left]):
                left += 1
            # skip over non-alphanumeric chars - don't go out of bounds/pass other pointer
            while right > left and not self.alpha_num(s[right]):
                right -= 1
            # if the characters at left and right position are not equal - not palindrome
            if s[left].lower() != s[right].lower():
                return False
            # move the pointers
            left += 1
            right -= 1
        # at this point it is a palindrome
        return True

    def alpha_num(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))