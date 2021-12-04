'''
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "xyzzaz"

x y z z a z
    ^
          ^

{y: 1, z: 2, a: 1}

Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4

a a b a b c a b c
^
          ^

Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
'''


class Solution:
    def countGoodSubstrings2(self, s: str) -> int:
        freq_map = dict()
        good_substr_count = 0
        window_start = 0

        if len(s) < 3:
            return 0

        for window_end in range(len(s)):
            elem = s[window_end]

            if elem not in freq_map:
                freq_map[elem] = 0
            freq_map[elem] += 1

            if len(freq_map) >= 3:

                while list(freq_map.values()) != [1, 1, 1] and len(freq_map) != 0 and window_start != window_end:

                    if len(freq_map) < 3:
                        break

                    left_elem = s[window_start]

                    if left_elem in freq_map:
                        freq_map[left_elem] -= 1

                    if freq_map[left_elem] == 0:
                        del freq_map[left_elem]

                    window_start += 1

                if len(freq_map) != 0 and list(freq_map.values()) == [1, 1, 1]:
                    good_substr_count += 1

                # if list(freq_map.values()) != [1, 1, 1]:
                #     window_start += 1

        return good_substr_count

    def countGoodSubstrings(self, s: str) -> int:
        item_one = s[0]
        item_two = s[1]
        item_three = s[2]
        good_string = 0

        for idx in range(3, len(s), 1):
            if item_one != item_two and item_two != item_three and item_one != item_three:
                good_string += 1

            item_one = item_two
            item_two = item_three
            item_three = s[idx]

        if item_one != item_two and item_two != item_three and item_one != item_three:
            good_string += 1

        return good_string


def main():
    assert Solution().countGoodSubstrings('xyzzaz') == 1
    assert Solution().countGoodSubstrings('aababcabc') == 4
    assert Solution().countGoodSubstrings('owuxoelszb') == 8
    assert Solution().countGoodSubstrings('npdrlvffzefb') == 8
    assert Solution().countGoodSubstrings('icolgrjedehnd') == 10
    assert Solution().countGoodSubstrings('aaaaaaaaaaaaaaaaabc') == 1


if __name__ == '__main__':
    main()
