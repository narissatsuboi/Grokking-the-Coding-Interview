
import unittest


def triplet_sums_to_zero(arr):
    """
    3 pointer approach
    1. iterate over each ele at index i, skip any duplicates
    2. find two numbers using left and right pointers (not ele at i)
       that sum to -ele at i
    3. if sum is smaller than - ele, increase left pointer
    4. if sum is larger than - ele, decrease right pointer
    5. store result in 2d array

    :param arr:
    :return: 2d array of result
    """
    # sort the array
    arr.sort()
    result = []  # stores result

    # iterate over each element i
    for i in range(len(arr)):
        # skip duplicates
        if i > 0 and arr[i] == arr[i-1]:
            continue
        # search for the two elements after i that add up to the target sum
        search_sum_pair(arr, -arr[i], result, i+1)
    # return result
    return result


def search_sum_pair(arr, target_sum, triplet, left):
    # left pointer is given to us from parent function
    right = len(arr) - 1  # initialize right pointer at end of array

    # iterate over subset of elements with left and right pointers
    # moving left and right toward each other
    # continue until sum is found or the pointers overlap

    while left < right:
        current_sum = arr[left] + arr[right]
        # sum found
        if current_sum == target_sum:
            # store triplet
            triplet.append([-target_sum, arr[left], arr[right]])
            # shift pointers inward and continue looking
            left += 1
            right -= 1
            # skip duplicates
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        # sum not found - shift pointers
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


class TestFindSum(unittest.TestCase):
    def test_triplet_sums_to_zero(self):
        self.assertEqual([[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]],
                         triplet_sums_to_zero([-3, 0, 1, 2, -1, 1, -2]))
        self.assertEqual([[-5, 2, 3], [-2, -1, 3]],
                         triplet_sums_to_zero([-5, 2, -1, -2, 3]))


if __name__ == '__main__':
    print("Triplet Sums to Zero")
    unittest.main(verbosity=2)
