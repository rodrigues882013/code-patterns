'''
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.

Example 1
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

'''

'''
Brute force version, complexity is O(n*k)
'''


def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    maximum = -1

    for i in range(0, len(arr) - k + 1):
        local_sum = arr[i]

        for j in range(i + 1, k + i):
            local_sum += arr[j]

        if local_sum < maximum:
            maximum = local_sum

    return maximum


'''
More smart approach complexity is O(k) + O(n-1)
'''


def max_sub_array_of_size_k_optimize(k: int, arr: list[int]) -> int:
    maximum = -1
    summ = 0

    for i in range(0, k):
        summ = arr[i]

    for j in range(1, len(arr)):
        local_sum = summ - arr[j - 1]
        local_sum += arr[j]

        if local_sum > maximum:
            maximum = local_sum

    return maximum


def main():
    print(max_sub_array_of_size_k_optimize(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k_optimize(2, [2, 3, 4, 1, 5]))


if __name__ == '__main__':
    main()
