"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2 []
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1, []
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3, []
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

"""


# O(n*n), very inefficient
def longest_substring_with_k_distinct(s, k):
    longest_substring = -1

    if len(s) < k:
        return len(s)

    for i in range(0, len(s)):
        sub = ""
        distinct_chars_already_add = set()

        for j in range(i, len(s)):
            if s[j] in distinct_chars_already_add:
                sub += s[j]
            else:
                if len(distinct_chars_already_add) < k:
                    sub += s[j]
                    distinct_chars_already_add.add(s[j])
                else:
                    longest_substring = max(longest_substring, len(sub))
                    break

    return longest_substring


def longest_substring_with_k_distinct_optimized(s, k):
    longest_substring = -1

    if len(s) < k:
        return len(s)

    runner = 0
    distinct_chars_already_add = dict()

    window_start = 0
    window_end = 0

    while runner < len(s):
        if s[runner] in distinct_chars_already_add:
            distinct_chars_already_add[s[runner]] += 1
            window_end += 1
            runner += 1

        elif len(distinct_chars_already_add.keys()) < k:
                distinct_chars_already_add[s[runner]] = 1
                window_end += 1
                runner += 1

        else:
            longest_substring = max(longest_substring, len(s[window_start:window_end]))
            distinct_chars_already_add[s[window_start]] -= 1

            if distinct_chars_already_add[s[window_start]] == 0:
                del distinct_chars_already_add[s[window_start]]

            window_start += 1
    
        
    
            

    return longest_substring


def main():
    print(longest_substring_with_k_distinct_optimized('araaci', 2))
    print(longest_substring_with_k_distinct_optimized('araaci', 1))
    print(longest_substring_with_k_distinct_optimized('cbbebi', 3))
    print(longest_substring_with_k_distinct_optimized('cbbebi', 10))


if __name__ == '__main__':
    main()
