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
"""


# Time complexity: O(s + t). Space Complexity: O(s + t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if both strings are not the same length then not anagram
        if len(s) != len(t):
            return False

        # create two hash maps to count character occurrences
        # letter: number of occurrences
        s_ltr_hash = {}
        t_ltr_hash = {}

        # use loop to update letter occurrences
        for i in range(len(s)):
            # use dict.get to avoid key error letter isn't in hash map yet
            s_ltr_hash[s[i]] = 1 + s_ltr_hash.get(s[i], 0)
            t_ltr_hash[t[i]] = 1 + t_ltr_hash.get(t[i], 0)

        # iterate through hash and see if occurrences match
        for j in s_ltr_hash:
            if s_ltr_hash[j] != t_ltr_hash.get(j, 0):
                return False

        return True
