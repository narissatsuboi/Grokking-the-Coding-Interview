"""
Given a sorted array, create a new array containing squares of all the numbers
of the input array in the sorted order.
"""

import unittest


def make_squares(arr):
    """
    2 pointer approach
    :param arr:
    :return: new array
    """
    n = len(arr)
    left = 0
    right = n - 1
    res = [None] * n  # resultant array
    i = n - 1  # result array loop control variable

    # square all elements in array
    arr = [ele ** 2 for ele in arr]

    while i >= 0:
        left_num = arr[left]
        right_num = arr[right]
        res[i] = max(left_num, right_num)
        if arr[left] >= arr[right]:
            left += 1
        else:
            right -= 1
        i -= 1
    return res


class TestMakeSquares(unittest.TestCase):
    def test_make_squares(self):
        # self.assertEqual([0, 1, 4, 4, 9], make_squares([-3, -1, 0, 1, 2]))
        self.assertEqual([], make_squares([]))


if __name__ == '__main__':
    unittest.main(verbosity=2)

