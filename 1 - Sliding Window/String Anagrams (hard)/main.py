"""
Given a string and a pattern, find all anagrams of the pattern
in the given string.

Every anagram is a permutation of a string. As we know, when we
are not allowed to repeat characters while finding permutations of
a string, we get N!N! permutations (or anagrams) of a string having
NN characters. For example, here are the six anagrams of the string
“abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the
anagrams of the pattern in the given string.
"""

from collections import Counter
import unittest


def string_anagrams(s, pattern):
    """
    Sliding window approach, track indices in list.
    1. Iterate over the length of the string
    2. Adjust frequency map when character is encountered
    3. Anagram occurs when len of pattern = number of matched chars
        Store index of window start in list.
    4. When window exceeds len of pattern, shrink window, adjust
        frequency of character removed from window (+1)
    :param s:
    :param pattern:
    :return:
    """

    window_start = 0  # left boundary of sliding window
    matched_chars = 0  # count of chars matched in the pattern map
    anagram_indices = []  # holds starting indices of anagram occurrences

    # fill character frequency map
    char_frequency = Counter(pattern)

    # extend the sliding window's end index along the length of the string s
    for window_end in range(len(s)):
        # store character at window's end index
        right_char = s[window_end]

        # check if character in pattern map
        if right_char in char_frequency:
            # decrement the frequency and update the count of matches
            char_frequency[right_char] -= 1

            if char_frequency[right_char] == 0:
                matched_chars += 1

        # check if the pattern has been completed matched
        if matched_chars == len(char_frequency):
            # store starting index in list
            anagram_indices.append(window_start)

        # pattern not complete, check if we need to shrink the window
        if window_end - window_start + 1 > len(pattern):
            # store character at window start
            left_char = s[window_start]
            window_start += 1  # advance window starting index

            # update frequency in pattern map and match accumulator
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched_chars -= 1
                char_frequency[left_char] += 1

    return anagram_indices


class TestStringAnagrams(unittest.TestCase):
    def test_string_anagrams(self):
        self.assertEqual([1, 2], string_anagrams("ppqp", "pq"))


if __name__ == '__main__':
    print("String Anagrams")
    unittest.main(verbosity=2)