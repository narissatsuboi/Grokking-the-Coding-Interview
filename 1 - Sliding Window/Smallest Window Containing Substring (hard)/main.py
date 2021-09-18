"""
Given a string and a pattern, find the smallest substring in the
given string which has all the characters of the given pattern.

"""

import unittest


class TestSmallestWindowSubstring(unittest.TestCase):
    def test_smallest_window_substring(self):
        self.assertEqual("abdec", smallest_window_substring("aabdec", "abc"))


def smallest_window_substring(s, pattern):
    """
    Sliding window approach

    :param s:
    :param pattern:
    :return: shortest substring containing letters from pattern
    """


if __name__ == '__main__':
    print("Smallest Window containing Substring")
    unittest.main(verbosity=2)