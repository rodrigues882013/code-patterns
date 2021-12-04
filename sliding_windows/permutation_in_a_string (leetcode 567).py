'''
Given a string and a pattern, find out if the string contains any permutation of the pattern

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

o i d b c a f
      ^
          ^

{b: 1, c: 1, a: 0}

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

'''

import copy

def count_freq(pattern):
    track_aux = {}

    for k in pattern:
        if k not in track_aux:
            track_aux[k] = 0
        track_aux[k] += 1

    return track_aux

def find_permutation(string, pattern):
    window_start = 0

    if string == pattern:
        return True

    immutable_track = count_freq(pattern)
    track_aux = copy.deepcopy(immutable_track)
    size = 0

    for window_end in range(len(string)):

        if string[window_end] in track_aux:
            track_aux[string[window_end]] -= 1

            if track_aux[string[window_end]] == 0:
                size += 1

        if size == len(track_aux):
            return True

        if window_end >= len(pattern) - 1:
            
            if string[window_start] in track_aux:
                
                if track_aux[string[window_start]] == 0:
                    size -= 1

                track_aux[string[window_start]] += 1

            window_start += 1

    return False


def main():
    print(find_permutation('oidbcaf','abc'))
    print(find_permutation('odicf','dc'))

    print(find_permutation('bcdxabcdy','bcdyabcdx'))
    print(find_permutation('aaacb','abc'))


    print(find_permutation('eidbaooo','ab'))
    print(find_permutation('eidboaoo','ab'))
    print(find_permutation('dcda','adc'))
 
    print(find_permutation('ooolleoooleh','hello'))
    '''
    o o o l l e o o o l e h
    ^
    ^

    {h: 1, e: 0, l: 0, o: 0}
    '''

if __name__ == '__main__':
    main()