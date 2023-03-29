"""
Write a function that takes the binary representation of an unsigned integer and returns the
number of '1' bits it has (also known as the Hamming weight).

Note:
    Note that in some languages, such as Java, there is no unsigned integer type. In this case,
    the input will be given as a signed integer type. It should not affect your implementation,
    as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore,
    in Example 3, the input represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1'
bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one
'1' bits.

Constraints:
    The input must be a binary string of length 32.

"""


# Time complexity: O(1). Space complexity O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        # run until n is 0 which is when all bits have shifted over
        while n:
            # % 2 will give us 1 or 0. 1 for when digit is 1 since 2 in binary is 0001.
            # we are 'anding' them so if both positions are 1 it will result in 1
            # we can simply add the result to itself since only answers are 0 and 1
            result += n % 2
            # shift the bits to the right by one to update the number and move over
            n = n >> 1
        # return the result which has counter the number of 1's
        return result
