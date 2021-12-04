"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pair = []
        end = len(nums) - 1
        start = 0

        while start != end:

            if nums[start] + nums[end] == target:
                pair = [start, end]
                break
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1

        return pair


def main():
    assert Solution().twoSum([1, 2, 3, 4, 6], 6) == [1, 3]
    assert Solution().twoSum([2, 5, 9, 11], 11) == [0, 2]
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([2, 3, 4], 6) == [0, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]


if __name__ == '__main__':
    main()