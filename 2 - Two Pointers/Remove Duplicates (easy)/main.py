"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates
in-place return the length of the subarray that has no duplicate in it.
"""

import unittest


def remove_duplicates(arr):
    """
    2 Pointer Approach

    :param arr:
    :return:

    """
    # slow pointer
    non_dup_index = 0  # accumulator tracks new length of sorted non-dup arr

    # i is the fast pointer
    for i in range(len(arr)):  # i pointer iterates through each ele
        if i < len(arr) - 2 and arr[i] == arr[i + 1]:
            continue  # skip past duplicates
        # update element next to the last non duplicate element
        arr[non_dup_index] = arr[i]
        # update slow pointer to next element
        non_dup_index += 1

    print(arr)
    return non_dup_index


if __name__ == '__main__':
    print("Remove Duplicates")
    arr = [2, 3, 3, 3, 6, 9, 9]
    print(arr)
    print(remove_duplicates(arr))
