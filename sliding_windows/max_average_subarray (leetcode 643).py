import math
from statistics import mean
from typing import List


class Solution:
    '''
    [1, 12, -5, -6, 50, 3]
            ^
                        ^
    '''
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start = 0
        window_end = 1
        max_avg = -math.inf
        summ = nums[0]
        count = 1

        if k == 1:
            max_avg = max(nums)

        else:

            while window_end <= len(nums) - 1:

                summ += nums[window_end]
                count += 1

                if count == k:
                    local_avg = summ / k
                    max_avg = max(local_avg, max_avg)
                    summ -= nums[window_start]
                    window_start += 1
                    count -= 1

                window_end += 1

        return max_avg


def main():
    assert Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert Solution().findMaxAverage([5], 1) == 5.00


if __name__ == '__main__':
    main()

