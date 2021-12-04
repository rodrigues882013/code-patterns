from typing import List

'''
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

0  1  2  3
1, 2, 3, 1
^
         ^

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

0  1  2  3  4  5
1, 2, 3, 1, 1, 3
^
            ^

{1: 3, 2: 1, 3: 2, }
'''


# O(len(nums) + 1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq_map = dict()

        for idx, val in enumerate(nums):
            if val not in freq_map:
                freq_map[val] = idx
            else:
                k_factor = abs(idx - freq_map[val])

                if k_factor <= k:
                    return True
                else:
                    freq_map[val] = idx

        return False


def main():
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False


if __name__ == '__main__':
    main()
