"""
Given a string and a pattern, find the smallest substring in the given string
which has all the characters of the given pattern.

Example 1
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

0 1 2 3 4 5
a a b d e c
  ^
          ^

{a: 0, b: 0, c: 0}

Example 2:
Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

0 1 2 3 4 5
a b d b c a
      ^
          ^
l = 1
r = 5
{a: 0, b: 0, c: 0}
matches = 3


Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

Example 4:
Input: String = "ADOBECODEBANC", Pattern = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from pattern.

0 1 2 3 4 5 6 7 8 9 10  11  12
A D O B E C O D E B  A  N   C
                  ^
                            ^

{A: 1, B: 1, C: 0}

Example 5:
Input: String = "a", Pattern = "a"
Output: "a"
Explanation: The entire string s is the minimum window.


Example 6:
Input: String = "a", Pattern = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""


def find_substring_grokking_solution(str1, pattern):
    """
    1) We will keep a running count of every matching instance of a character.
    2) Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track
       of the smallest substring that has all the matching characters.
    3) We will stop the shrinking process as soon as we remove a matched character from the sliding window.
       One thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’
       in the sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’,
       we will simply shrink the window without decrementing the matched count.
       We will decrement the matched count when the second ‘a’ goes out of the window.
    """
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0

        char_frequency[char] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1

            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):

            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1

            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1

                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""

    return str1[substr_start:substr_start + min_length]


def count_freq(pattern: str) -> dict:
    track_aux = {}

    for k in pattern:
        if k not in track_aux:
            track_aux[k] = 0
        track_aux[k] += 1

    return track_aux


def calculate_size(window_start: int, window_end: int, smallest_window_start: int,
                   smallest_window_end: int, smallest_window_size: int) -> tuple[int, int, int]:
    # Get calculate the current window size
    current_window_size = window_end - window_start + 1

    smallest_window_start_candidate = smallest_window_start
    smallest_window_end_candidate = smallest_window_end
    smallest_window_size_candidate = smallest_window_size

    # Just update if the new windows size is greater then the old one
    if smallest_window_size >= current_window_size:
        smallest_window_start_candidate = window_start
        smallest_window_end_candidate = window_end
        smallest_window_size_candidate = current_window_size

    return smallest_window_start_candidate, smallest_window_end_candidate, smallest_window_size_candidate


def does_string_have_all_chars_in_pattern(pattern: str, string: str) -> bool:
    for char in pattern:
        if char not in string:
            return False

    return True


def is_window_valid(track: dict) -> bool:
    track_values = list(track.values())
    return len(list(filter(lambda item: item <= 0, track_values))) == len(track_values)


# O(len(s) + len(pattern))
def find_substring(string: str, pattern: str) -> str:
    # Get calculate the initial parameters
    smallest_window_start = 0
    smallest_window_end = len(string) - 1 if len(string) > 0 else -1
    smallest_window_size = smallest_window_end - smallest_window_start + 1
    window_start = 0

    if string == pattern:
        return pattern

    if len(pattern) > len(string) or \
            smallest_window_end == -1 or \
            not does_string_have_all_chars_in_pattern(pattern, string):
        return ''

    track = count_freq(pattern)
    matches = 0
    pattern_exist_at_least_once = False

    for window_end in range(len(string)):

        if string[window_end] in track:
            track[string[window_end]] -= 1
            matches += 1

        if is_window_valid(track):
            pattern_exist_at_least_once = True

            params = dict(
                window_start=window_start,
                window_end=window_end,
                smallest_window_start=smallest_window_start,
                smallest_window_end=smallest_window_end,
                smallest_window_size=smallest_window_size)

            smallest_window_start, smallest_window_end, smallest_window_size = calculate_size(**params)

            while is_window_valid(track):

                params = dict(
                    window_start=window_start,
                    window_end=window_end,
                    smallest_window_start=smallest_window_start,
                    smallest_window_end=smallest_window_end,
                    smallest_window_size=smallest_window_size)

                smallest_window_start, smallest_window_end, smallest_window_size = calculate_size(**params)

                if string[window_start] in track:
                    matches -= 1
                    track[string[window_start]] += 1

                window_start += 1

    if not pattern_exist_at_least_once:
        return ''

    return "".join(string[smallest_window_start:smallest_window_end + 1])


def main():
    print(find_substring('aabdec', 'abc') == 'abdec')
    print(find_substring('abdbca', 'abc') == 'bca')
    print(find_substring('adcad', 'abc') == '')  # see
    print(find_substring('a', 'a') == 'a')
    print(find_substring('a', 'aa') == '')
    print(find_substring('ab', 'a') == 'a')
    print(find_substring('ab', 'b') == 'b')
    print(find_substring('ADOBECODEBANC', 'ABC') == 'BANC')
    print(find_substring('bbaa', 'aba') == 'baa')
    print(find_substring('bbaac', 'aba') == 'baa')
    print(find_substring('cabwefgewcwaefgcf', 'cae') == 'cwae')
    print(find_substring('babb', 'baba') == '')


if __name__ == '__main__':
    main()
