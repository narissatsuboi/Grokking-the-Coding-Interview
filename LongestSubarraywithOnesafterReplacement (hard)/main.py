"""
Given an array containing 0s and 1s, if you are allowed to replace
no more than ‘k’ 0s with 1s, find the length of the longest contiguous
subarray having all 1s.
"""
import unittest


def longest_subarray_with_ones(K, str):
    """
    Sliding Window Approach.
    Condition: Can replace K 0s with 1s. Shrink window when window size -
    repeating ones count > K replacements.
    :param K: number of allotted replacements
    :param str: string of lowercase letters
    :return: max window length
    """

    window_start = 0  # left boundary of sliding window
    repeating_ones_count = 0  # count of continuous ones within the window
    max_len = 0  # max length of subarray under given condition

    for window_end in range(len(str)):
        right_digit = str[window_end]
        if right_digit == 1:
            repeating_ones_count += 1

        # shrink window if more than k replacements needed
        if window_end - window_start + 1 - repeating_ones_count > K:
            left_digit = str[window_start]
            if left_digit == 1:
                repeating_ones_count -= 1
            window_start += 1

        # calculate max len
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


class TestLongestSubArraywithOnes(unittest.TestCase):
    def test_longest_subarray_with_ones(self):
        self.assertEqual(6, longest_subarray_with_ones(2, [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]))


if __name__ == '__main__':
    print("Longest Subarray with Ones after Replacement")
    unittest.main(verbosity=2)
