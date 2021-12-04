"""
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and
return the new length of the array.

Example 1:
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

2, 6, 10, 9, 3, 3, 3, 3
             ^
                       ^

Example 2:
Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].

11, 1, 2, 2, 2
       ^
                ^

"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] != val:
                pivot = nums[left]
                nums[left] = nums[right]
                nums[right] = pivot
                left += 1
            right += 1

        return left

def main():
    assert Solution().removeElement([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4
    assert Solution().removeElement([2, 11, 2, 2, 1], 2) == 2

if __name__ == '__main__':
    main()
