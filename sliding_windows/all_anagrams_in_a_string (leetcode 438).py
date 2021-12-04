'''
Given a string and a pattern, find all anagrams of the pattern in the given string.
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

p p q p
    ^
      ^



Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

0 1 2 3 4 5 6 7 8
a b c v x a b a c        [0, 6]
  ^
    ^

{a: 0, b: 0, c: 0}

1)

'''

from typing import List


def count_freq(pattern):
    track_aux = {}

    for k in pattern:
        if k not in track_aux:
            track_aux[k] = 0
        track_aux[k] += 1

    return track_aux

def find_string_anagrams(string: str, pattern: str) -> List[int]:
    result_indexes = []
    window_start = 0

    if string == pattern:
        return True

    track = count_freq(pattern)
    matches = 0

    for window_end in range(len(string)):

        if string[window_end] in track:
            track[string[window_end]] -= 1

            if track[string[window_end]] == 0:
                matches += 1

        if matches == len(track):
            result_indexes.append(window_start)

        if window_end >= len(pattern) - 1:
            
            if string[window_start] in track:
                
                if track[string[window_start]] == 0:
                    matches -= 1

                track[string[window_start]] += 1

            window_start += 1


    return result_indexes

def main():
    print(find_string_anagrams('ppqp','pq'))
    print(find_string_anagrams('abbcabc','abc'))
    print(find_string_anagrams('abcvxabac','abc'))


    
    

if __name__ == '__main__':
    main()