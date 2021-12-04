'''
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, 
find the length of the longest substring having the same letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

a a b c c b b 
a a b c c b b
    ^
            ^
            ^


a b b c b
  ^
        ^
        ^

a b c c d e
        ^
        ^
          ^


A A B A B B A
            ^
            ^
            ^

A B A B
^
      ^
      ^

'''

import copy

def is_window_valid(window_start, window_end, most_freq, k):
    return (window_end - window_start + 1) - most_freq <= k

def length_of_longest_substring(s, k):
    window_start = 0
    max_length = 0
    char_counts = {}
    most_freq_count = 0

    for window_end in range(len(s)):
        if s[window_end] in char_counts:
            char_counts[s[window_end]] += 1
        
        else:
            char_counts[s[window_end]] = 1

        most_freq_count = max(most_freq_count, char_counts[s[window_end]])

        while not is_window_valid(window_start, window_end, most_freq_count, k):
            char_counts[s[window_start]] -= 1
            window_start += 1
            
        max_length = max(max_length, window_end - window_start + 1)

    return max_length



def main():
    #print(length_of_longest_substring('aabccbb', 2))
    #print(length_of_longest_substring('abbcb', 1))
    # print(length_of_longest_substring('abccde', 1))
    # print(length_of_longest_substring('ABAB', 2))
    # print(length_of_longest_substring('AABABBA', 1))
    # print(length_of_longest_substring('AABA', 0))
    # print(length_of_longest_substring('AAAA', 0))
    print(length_of_longest_substring('ABAA', 0))
    #print(non_repeat_substring('abccde'))
    #print(non_repeat_substring('dvdf'))
    #print(non_repeat_substring("anviaj"))
    #print(non_repeat_substring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

    


if __name__ == '__main__':

    main()