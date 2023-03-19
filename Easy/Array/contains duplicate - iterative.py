"""
Given an integer array nums, return true if any value appears at least twice in the array, and
return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


# time complexity: O(n^2). Space complexity O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

