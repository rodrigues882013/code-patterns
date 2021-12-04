
'''
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".


Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".

[a] a b c c b b

track {a: 1}
window_start = 0
window_end = 1
'''
def non_repeat_substring_2(s: str) -> int:

    max_length = -1
    track = {}
    window_start = 0
    window_end = -1

    for runner in range(len(s)):
        if s[runner] not in track:
            track[s[runner]] = 1 
            window_end += 1   
        
        else:
            while window_start < window_end and s[runner] in track:
                track[s[window_start]] -= 1

                if track[s[window_start]] == 0:
                    del track[s[window_start]]
                
                window_start += 1


            if s[runner] not in track:
                track[s[runner]] = 1 
                window_end += 1

            else:
                window_start += 1 
                window_end += 1            


        max_length = max(max_length, (window_end - window_start) + 1)

    return max_length


# Grokking's solution

def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):

    right_char = str1[window_end]

    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:

      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)

    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end

    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)

  return max_length


def main():
    print(non_repeat_substring('aabccbb'))
    #print(non_repeat_substring('abbbb'))
    #print(non_repeat_substring('abccde'))
    #print(non_repeat_substring('dvdf'))
    #print(non_repeat_substring("anviaj"))
    #print(non_repeat_substring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

    


if __name__ == '__main__':
    main()