"""
Given an array arr of unsorted numbers and a target sum, count all triplets
in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three
different indices. Write a function to return the count of such triplets.
"""

import unittest


def triplets_with_smaller_sum(arr, target):
    """
    3 pointer approach.
    Sort the array.
    1st pointer iterates over nums in array.
    2nd and 3rd pointers iterate between 1st pointer and end of array.
        Check for sum found.
        Sum Found...
            Skip duplicates.
            Increment counter.
        Sum Not Found...
            Shift 2nd and 3rd pointers.
    Return counter of triplets found.
    :param arr: array of unsorted numbers
    :param target_sum: For condition X + Y + Z < target_sum
    :return: count of triplets meeting condition
    """

    count = 0  # result

    # sort the array to prep for pointer approach
    arr.sort()

    # iterate first pointer over nums in array
    for i in range(len(arr)):
        # call find pairs
        count += find_pair_sums_less_than(arr, target - arr[i], i+1)

    return count


def find_pair_sums_less_than(arr, target_sum, left):
    """

    :param arr:
    :param target_sum:
    :param left: points to num after num at i from parent function
    :param count: number of valid triples found
    :return:
    """
    count = 0
    right = len(arr) - 1  # initialize right pointer to end of array
    while left < right:

        # if sum is found, increment count accumulator
        # all numbers between left and right pointers are valid, so include
        # them all in the accumulator
        if target_sum > arr[left] + arr[right]:
            count += right - left
            left += 1
        # if sum is not found, shift right pointer to decrease the sum
        else:
            right -= 1

    return count


class TestTripletswithSmallerSum(unittest.TestCase):
    def test_triplets_with_smaller_sum(self):
        self.assertEqual(2, triplets_with_smaller_sum([-1, 0, 2, 3], 3))
        self.assertEqual(4, triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))


if __name__ == '__main__':
    print("TripletswithSmallerSum")
    unittest.main(verbosity=2)
