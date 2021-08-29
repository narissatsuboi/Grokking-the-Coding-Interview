"""
Given a string, find the length of the longest substring
in it with no more than K distinct characters.

You can assume that K is less than or equal to the length
of the given string.
"""

import unittest


def longest_substring_with_k_distinct(K, str):
    window_start = 0  # left bound of sliding window
    max_length = 0  # current longest length of substring with k distinct
    char_frequency_map = {}  # hashmap stores frequency of each char in the
    # str

    # extend window boundaries and store character frequencies in hash map
    for window_end in range(len(str)):
        right_char = str[window_end]  # get next character in str

        # print(str[window_start:window_end])
        # print(char_frequency_map)
        # print()

        # reset frequency hash map to 0 if character not in map
        # this means there are no instances of this character
        # in the current sliding window
        if right_char not in char_frequency_map:
            char_frequency_map[right_char] = 0
        char_frequency_map[right_char] += 1  # increase frequency

        # shrink the sliding window when more than k chars are in map
        while len(char_frequency_map) > K:

            # decrement the frequency of the character at window_start
            left_char = str[window_start]
            char_frequency_map[left_char] -= 1

            # remove char from map if count is 0
            if char_frequency_map[left_char] == 0:
                del char_frequency_map[left_char]

            # shrink the window to eclipse the character whose frequency
            # was decremented
            window_start += 1

        # store the maximum length
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


class TestLongestSubstringWithKDistinct(unittest.TestCase):
    def test_longest_substring_with_k_distinct(self):
        self.assertEqual(4, longest_substring_with_k_distinct(2, "araaci"))
        self.assertEqual(2, longest_substring_with_k_distinct(1, "araaci"))
        self.assertEqual(5, longest_substring_with_k_distinct(3, "cbbebi"))


if __name__ == '__main__':
    print("Longest Substring with K Distinct Characters")
    unittest.main(verbosity=2)



