from collections import deque

"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of
the earliest occurrence. If there are none, return an empty string.

Example 1
Input: s = "YazaAay"

Y a z a A a y
^
  ^
    
{a: 2, A:1, y: 1}

{Y: 0, a:3: A: 1, y: 1}
Output: "aAa"

Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

Example 4:
Input: s = "dDzeE"
Output: "dD"
Explanation: Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.

"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        freq_map = dict()
        window_start = 0
        nice_substr = deque([])

        for _, val in enumerate(s):
            if val not in freq_map:
                freq_map[val] = 0
            freq_map[val] += 1

        for window_end in range(len(s)):
            elem = s[window_end]

            if elem.upper() not in freq_map and elem.lower() not in freq_map:
                window_start = window_end + 1
                continue

        return nice_substr.popleft()

    def longestNiceSubstringBruteForce(self, s: str) -> str:
        freq_map = dict()
        window_start = 0
        nice_substr = deque([])

        for idx in range(len(s) - 1):


            for jdx in range(idx + 1, len(s), 1):
                freq_map = {}
                substr = s[idx: jdx + 1]

                for xdx in substr:
                    if xdx not in freq_map:
                        freq_map[xdx] = 0
                    freq_map[xdx] += 1

                for xdx in substr:
                    if xdx.upper() not in freq_map or xdx.lower() not in freq_map:
                        break

                if len(freq_map) % 2 == 0:
                    print(substr)
        return ''


def main():
    assert Solution().longestNiceSubstringBruteForce('YazaAay') == 'aAa'

if __name__ == '__main__':
    main()