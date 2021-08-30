"""
Given an array of sorted numbers and a target sum, find a pair in the
array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair)
such that they add up to the given target.
"""

import unittest


def pair_with_target_sum(arr, target):
    """
    Two Pointer Approach.
    Start pointer and end pointer.
    If sum of the numbers is bigger than the sum, move end pointer left.
    If sum of the numbers is smaller than the sum, move start pointer right.

    :param arr: an array of sorted numbers
    :param target: sum to search for
    :return: indices of elements
    """

    result = []  # indices of two elements matching the target sum
    end = len(arr) - 1  # end pointer, moves left

    for start in range(len(arr)):
        sum_ = arr[start] + arr[end]

        # check for match to target sum
        if sum_ == target:
            result.append(start)
            result.append(end)
            return result
        # adjust end pointer
        elif sum_ > target:
            end -= 1
        # adjust start pointer
        else:
            start += 1

    # if not found
    if not result:
        return -1


class TestPairwithTargetSum(unittest.TestCase):
    def test_pair_with_target_sum(self):
        self.assertEqual(-1, pair_with_target_sum([1, 1, 1], 7))  # not
        # found condition
        self.assertEqual([1, 3], pair_with_target_sum([1, 2, 3, 4, 6], 6))


if __name__ == '__main__':
    print("Pair with Target Sum")
    unittest.main(verbosity=2)

