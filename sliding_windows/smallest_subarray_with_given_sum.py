import sys

'''
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
 Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].

'''

'''
Brute force version, complexity is O(n*n)
'''


def smallest_subarray_with_given_sum(s, arr):
    minimum = sys.maxsize

    for i in range(0, len(arr)):

        summ = arr[i]
        size = 1

        if i == len(arr) - 1 and arr[i] >= s:
            minimum = min(size, minimum)

        for j in range(i + 1, len(arr)):
            summ += arr[j]
            size += 1

            if summ >= s:
                minimum = min(size, minimum)
                break

    return minimum


'''
K = number of times which my sum overflow the target value

T(n) = O(n * k)
'''


def smallest_subarray_with_given_sum_optimize(s: int, arr: list[int]) -> int:
    minimum = sys.maxsize
    window_size, window_start, summ = 0, 0, 0

    k = 1
    for i in range(0, len(arr)):
        window_size += 1
        summ += arr[i]

        while summ >= s:
            minimum = min(minimum, i - window_start + 1)
            summ -= arr[window_start]
            window_start += 1
            k += 1

        k += 1

    if minimum == sys.maxsize:
        minimum = 0

    print(k)
    return minimum


def main():
    # print(smallest_subarray_with_given_sum_optimize(7, [2, 3, 1, 2, 3, 2]))
    # print(smallest_subarray_with_given_sum_optimize(7, [2, 1, 5, 2, 8]))
    print(smallest_subarray_with_given_sum_optimize(8, [3, 4, 1, 1, 6]))
    # print(smallest_subarray_with_given_sum_optimize(4, [1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    main()
