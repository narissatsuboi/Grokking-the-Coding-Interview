"""
Given a string, find the length of the longest substring,
which has no repeating characters.
"""

import unittest


def no_repeat_substring(str):
    """
    Sliding Window Approach with HashMap.
    :param str:
    :return: max. length of substring with non repeating chars
    """

    window_start = 0  # holds left boundary of valid substring window
    max_len = 0  # holds maximum length of non repeating chars
    char_index_map = {}  # holds indexes of character keys

    # iterate through the length of the string, each iteration slides the
    # window end boundary
    for window_end in range(len(str)):
        right_char = str[window_end]  # char at window end

        # check if right char has been accounted for in substring
        # slide window start until right char isn't repeated
        if right_char in char_index_map:
            # window_start - char no longer in current window
            # char_index_map[right_char] + 1, next char after previous
            # occurrence
            window_start = max(window_start, char_index_map[right_char] + 1)

        # record index of right character
        char_index_map[right_char] = window_end

        # update max length
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


class TestNoRepeatSubstring(unittest.TestCase):
    def test_no_repeat_substring(self):
        self.assertEqual(0, no_repeat_substring(""))
        self.assertEqual(3, no_repeat_substring("aabccbb"))
        self.assertEqual(2, no_repeat_substring("abbbb"))
        self.assertEqual(3, no_repeat_substring("abccde"))


if __name__ == '__main__':
    print("Non Repeating Substring")
    unittest.main(verbosity=2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
