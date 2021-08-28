"""
Given an array of positive numbers and a positive number ‘k,’
find the maximum sum of any contiguous subarray of size ‘k’.
"""

import unittest


def find_subarray_maxSum(K, arr):
    """
    Finds the maximum sum from subarrays of size K
    Sliding window approach. For each window of size K, add
    the next element in the array and subtract the previous.
    :param K: subarray size
    :param arr:
    :return: maximum sum of K subarrays

    Time: O(N)
    Space: O(1)
    """

    result = []  # holds all sums of K subarrays
    windowStart = 0  # index of current starting bound of window
    windowSum = 0.0  # holds sum of current window
    maxSum = 0  # holds current maximums sum of subarray

    # iterate through windowEnd O(N)
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # we only want to sum and shift a window when the window is size K+
        if windowEnd >= K - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]  # subtract overlapping element
            windowStart += 1  # shift window start 1 element

    return maxSum


class TestMaxSumMethods(unittest.TestCase):
    def test_find_subarray_maxSum(self):
        self.assertEqual(9, find_subarray_maxSum(3, [2, 1, 5, 1, 3, 2]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Maximum Sum Subarray of Size K")
