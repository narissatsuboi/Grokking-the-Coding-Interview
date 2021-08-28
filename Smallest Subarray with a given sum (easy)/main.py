
"""
Given an array of positive numbers and a positive
number ‘S,’ find the length of the smallest contiguous
subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.
"""

import unittest
import math


def find_smallest_subarray(S, arr):
    """
    Find the smallest subarray in which the sum of the
    elements are greater than are equal to S.
    Sliding window approach.
    :param S: give sum to match or exceed
    :param arr:
    :return: length of smallest subarrray that meets criteria
    """

    window_sum = 0
    window_start = 0  # starting index for sliding window
    window_size = math.inf  # holds current smallest size of subarray

    # iterate through array
    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        #  add elements to window sum until greater than or equal to S
        while window_sum >= S:
            #  update current smallest window size
            window_size = min(window_size, window_end - window_start + 1)
            # shrink window
            window_sum -= arr[window_start]
            window_start += 1

    # not found condition
    if window_size == math.inf:
        return 0

    return window_size


class TestSmallestSubarray(unittest.TestCase):
    def test_find_smallest_subarray(self):
        self.assertEqual(2, find_smallest_subarray(7, [2, 1, 5, 2, 3, 2]))
        self.assertEqual(1, find_smallest_subarray(7, [2, 1, 5, 2, 8]))
        self.assertEqual(0, find_smallest_subarray(7, [1, 1, 1, 1 ,1]))



if __name__ == '__main__':
    print('Smallest Subarray with a given sum (easy)')
    unittest.main(verbosity=2)
