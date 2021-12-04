from typing import List
'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more 
than once in a DNA molecule. You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

fr = {AAAAACCCCC: 1, }

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_size = 10
        freq_map = {}
        distinct_seq = set()

        for idx in range(len(s)):
            substr = s[idx: idx + sequence_size]

            if substr not in freq_map:
                freq_map[substr] = 0

            freq_map[substr] += 1

            if freq_map[substr] > 1:
                distinct_seq.add(substr)

        return list(distinct_seq)


def main():
    assert Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"]
    assert Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA") == ["AAAAAAAAAA"]


if __name__ == '__main__':
    main()
