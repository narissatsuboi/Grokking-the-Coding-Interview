"""
Given a string with lowercase letters only, if you are allowed
to replace no more than ‘k’ letters with any letter, find the
length of the longest substring having the same letters after replacement.
"""

import unittest


def longest_substring_same_letters(K, str):
    """
    Sliding Window approach with limiting condition.
    Condition: Window size - consecutive characters < K.
    :param K: number of replacements allowed
    :param str: string containing lowercase letters
    :return: max length of string under condition
    """

    window_start = 0  # left boundary of sliding window
    repeat_char_count = 0  # consective characters not requiring replacement
    char_freq_map = {}  # holds counts of each character in window
    max_length = 0  # len of longest substring found under condition

    # extend right window boundary along the length of the string
    for window_end in range(len(str)):
        right_char = str[window_end]

        # store character frequency in HashMap for later use in condition check
        if right_char not in char_freq_map:
            char_freq_map[right_char] = 0
        char_freq_map[right_char] += 1

        # determine current longest length of repeating characters
        repeat_char_count = max(repeat_char_count, char_freq_map[right_char])

        # enforce boundary condition
        if window_end - window_start + 1 - repeat_char_count > K:
            # shift window start to the right
            left_char = str[window_start]
            char_freq_map[left_char] -= 1
            window_start += 1

        # determine current maximum length, the prev or current window size
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


class TestLongestSubstringSameLetters(unittest.TestCase):
    def test_longest_substring_same_letters(self):
        self.assertEqual(5, longest_substring_same_letters(2, "aabccbb"))


if __name__ == '__main__':
    print("Longest Substring with Same Letters after Replacement")
    unittest.main(verbosity=2)
