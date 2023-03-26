"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""


# Time complexity: O(n). Space complexity: O(1)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # making the string a set makes a list with each char as index
        for i in set(ransomNote):
            # check the number of count of each letter in both strings to determine
            # if the magazine letters can create the ransom note
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
