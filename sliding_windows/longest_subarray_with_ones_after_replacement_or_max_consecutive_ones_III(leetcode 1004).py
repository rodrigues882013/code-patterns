
'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.


Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1
^
         ^


{0: 1}
'''

def is_window_valid(zeros_counts, k):
    return zeros_counts <= k

def length_of_longest_substring(arr, k):
    window_start = 0
    max_length = 0
    zeros_counts = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 0:
            zeros_counts += 1
            
        while not is_window_valid(zeros_counts, k):
            if arr[window_start] == 0:
                zeros_counts -= 1

            window_start += 1
            
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    #print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    #print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
    print(length_of_longest_substring([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    #print(length_of_longest_substring('abbcb', 1))
    # print(length_of_longest_substring('abccde', 1))
    # print(length_of_longest_substring('ABAB', 2))
    # print(length_of_longest_substring('AABABBA', 1))
    # print(length_of_longest_substring('AABA', 0))
    # print(length_of_longest_substring('AAAA', 0))
    #print(non_repeat_substring('abccde'))
    #print(non_repeat_substring('dvdf'))
    #print(non_repeat_substring("anviaj"))
    #print(non_repeat_substring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

if __name__ == '__main__':
    main()