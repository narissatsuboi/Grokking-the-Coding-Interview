"""
Given a string and a pattern, find out if the string contains any permutation
 of the pattern.

Permutation is defined as the re-arranging of the characters of the string.
For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba

If a string has ‘n’ distinct characters, it will have n! permutations.
"""

from collections import Counter
import unittest


class TestFindPermutation(unittest.TestCase):
    def test_find_permutation(self):
        self.assertEqual(True, find_permutation("oidbcaf", "abc"))
        self.assertEqual(False, find_permutation("odicf", "dc"))
        self.assertEqual(True, find_permutation("bcdxabcdy", "bcdyabcdx"))

def find_permutation(_str, pattern):
    """
    Sliding window approach.
    :param _str:
    :param pattern: substring
    :return: True if permuation of pattern exists in string
    """

    window_start = 0  # left boundary of sliding window
    matched_chars = 0

    # fill frequency map for pattern with loop or Counter
    pattern_char_freq = Counter(pattern)

    # extend the right bound of the window one element at a time
    for window_end in range(len(_str)):
        right_char = _str[window_end]
        if right_char in pattern_char_freq:
            pattern_char_freq[right_char] -= 1  # decrement count from pattern

            # check if the count of this character has reached zero yet, if so,
            # all instances of this character in the pattern have been
            # matched in the window
            if pattern_char_freq[right_char] == 0:
                matched_chars += 1

        # check if the whole pattern has been matched
        # full match occurs when the count of matched chars is the same as
        # the length of the pattern
        if len(pattern)  == matched_chars:
            return True

        # adjust window length as necessary
        if window_end - window_start + 1 > len(pattern):
            left_char = _str[window_start]
            window_start += 1
            # adjust counts for removal of a char thats in the pattern
            if left_char in pattern_char_freq:
                if pattern_char_freq[left_char] == 0:
                    matched_chars -= 1
                pattern_char_freq[left_char] += 1

    return False

if __name__ == '__main__':
    print("String Permutations")
    unittest.main(verbosity=2)
