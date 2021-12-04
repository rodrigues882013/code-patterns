import math
from typing import List
from heapq import heappop, heappush, heapify
from collections import deque, OrderedDict
import bisect
from sortedcontainers import SortedList


'''
Given an integer array nums and two integers k and t, 
return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
i > k + j
nums[j] > nums[i] - t

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true


0  1  2  3
1, 2, 3, 1
   ^
      ^

{2: 1, 3: 2}

2 - 1

3 - 1
3 - 2

1 - 1
1 - 2
1 - 3



Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

0  1  2  3  4  5  
1, 5, 9, 1, 5, 9
   ^
         ^          

{1: []}
{1:0, 5: 1}
[1]

1-3 = 2
5-3 = 2
9-3 = 6

{1: [1, 2, 3, 4, 5], 5:[2, 5], 9:[5]}

<= 4



'''


# O(len(nums) + len(visited_items))
class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        freq_map = dict()
        window = OrderedDict()

        for idx, val in enumerate(nums):
            if val in freq_map or \
                    val - 1 in freq_map and abs(val - freq_map[val - 1]) <= t or \
                    val + 1 in freq_map and abs(val - freq_map[val + 1]) <= t:
                return True

            if len(freq_map) >= k:
                del nums[idx - k]

            freq_map[val] = idx

        return False


def main():
    # assert Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0) is True
    # assert Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2) is True
    # #assert Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
    # assert Solution().containsNearbyAlmostDuplicate([1, 2], 0, 1) is False
    # assert Solution().containsNearbyAlmostDuplicate([-1, -1], 1, 0) is True
    # assert Solution().containsNearbyAlmostDuplicate([1, 2, 1, 1], 1, 0) is True
    # assert Solution().containsNearbyAlmostDuplicate([1, 2, 5, 6, 7, 2, 4], 4, 0) is True
    #
    with open('large_test_case_leetcode (220)') as f:
            array = list(map(lambda x: int(x), f.readline().split(',')))
            assert Solution().containsNearbyAlmostDuplicate(array, 10000, 0) is False

    '''
     0  1
    [1, 2]
    
    {1: 0, 2: 1}
    [1]
    
    '''


if __name__ == '__main__':
    main()
