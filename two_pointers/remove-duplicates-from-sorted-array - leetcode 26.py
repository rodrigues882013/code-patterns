"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

2, 3, 6, 9, 9, 9, 9
            ^
                    ^


Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

"""
from typing import List


class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        next_non_duplicate = 0

        i = 1
        while i < len(arr):
            if arr[next_non_duplicate] != arr[i]:
                arr[next_non_duplicate + 1] = arr[i]
                next_non_duplicate += 1
            i += 1

        return next_non_duplicate + 1


def main():
    assert Solution().removeDuplicates([2, 3, 3, 3, 6, 9, 9]) == 4
    assert Solution().removeDuplicates([2, 2, 2, 11]) == 2
    assert Solution().removeDuplicates([1, 1, 2]) == 2
    assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5


if __name__ == '__main__':
    main()
