"""
Given a string and a list of words, find all the starting indices of substrings in the given string
that are a concatenation of all the given words exactly once without any overlapping of words.
It is given that all words are of the same length.

Example 1:
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

cat fox cat
 ^
     ^

{cat=1, fox=0}

Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".

cat cat fox fox
     ^
         ^

{cat=-1, fox=0}
matches = 3

word good good good best word
           ^
                          ^

{good: 0, word: 0, best: 0}
matches = 3
s = [8]


bar foo the foo bar man
         ^
             ^

{foo: 0, bar: 1}
matches = 2
s = [0]
"""
import functools
from typing import List


def count_freq(patterns: list) -> dict:
    track_aux = {}

    for k in patterns:
        if k not in track_aux:
            track_aux[k] = 0
        track_aux[k] += 1

    return track_aux


def is_window_valid(track: dict) -> bool:
    track_values = list(track.values())
    return len(list(filter(lambda item: item == 0, track_values))) == len(track_values)


def sum_freq(track: dict) -> int:
    track_values = list(track.values())
    return functools.reduce(lambda x, y: x + y, track_values, 0)


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        start_positions = []
        freq = count_freq(words)

        for idx in range((len(s) - len(words) * len(words[0])) + 1):
            substr_gt = s[idx: idx + len(words) * len(words[0])]
            words_seen = {}

            for jdx in range(0, len(substr_gt), len(words[0])):
                substr = substr_gt[jdx: jdx + len(words[0])]

                if substr not in freq:
                    break

                if substr not in words_seen:
                    words_seen[substr] = 0

                words_seen[substr] += 1

                if words_seen[substr] > freq.get(substr, 0):
                    break

            if words_seen == freq:
                start_positions.append(idx)

        return start_positions


def main():
    assert Solution().findSubstring('catfoxcat', ['cat', 'fox']) == [0, 3]
    assert Solution().findSubstring('catcatfoxfox', ['cat', 'fox']) == [3]
    assert Solution().findSubstring('barfoothefoobarman', ['foo', 'bar']) == [0, 9]
    assert Solution().findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']) == []
    assert Solution().findSubstring('barfoofoobarthefoobarman', ['bar', 'foo', 'the']) == [6, 9, 12] or [6, 12, 9]
    assert Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]
    assert Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]) == [13]
    assert Solution().findSubstring("ababababab", ["ababa", "babab"]) == [0]
    assert Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert Solution().findSubstring("aaaaaaaaaaaaaa", ["aa"]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert Solution().findSubstring("a", ["a"]) == [0]
    assert Solution().findSubstring("a", ["a", "a"]) == []
    assert Solution().findSubstring("aaa", ["a", "a"]) == [0, 1]






'''
0 1 2 3 4 5 6 7 8 9 10  11  12  13
a a a a a a a a a a  a   a   a   a
^
  ^ 

{aa: 2}
{aa: 1}
'''


if __name__ == '__main__':
    main()
