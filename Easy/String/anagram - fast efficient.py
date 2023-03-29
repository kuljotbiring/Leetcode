"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
"""


# Time complexity: O(n). Space Complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths don't match - not anagram
        if len(s) != len(t):
            return False

        # break one word into set to get unique chars
        for char in set(s):
            # if their counts not same - not anagram
            if s.count(char) != t.count(char):
                return False
        # at this point it's an anagram
        return True
