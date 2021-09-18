import math


def find_max_sum_subarray(arr, k=3):
    """
    Sliding window problem.
    Constraints: (1) Maximum sum (2) Fixed subarray size
    :param arr: array of integers greater than 0
    :param k: subarray size
    :return: maximum subarray sum

    0. iterate array, updating current_running_sum at each iteration
    1. check if the window meets the constraint size
        # valid window when i >= k - 1
    2. compare max_sum with current_running_sum, update max_sum
    3. shrink left side of the window
    4. subtract the leftmost element of the current window from
       current_running_sum
        # current index - (k - 1) <- bc k is a len and i is an indx
    """

    max_sum = -math.inf  # initial value neg. infinity
    current_running_sum = 0  # holds the total window sum

    for i in range(len(arr)):
        current_running_sum += arr[i]  # collect running sum every iteration
        if i >= (k - 1):  # compare index to window size
            max_sum = max(max_sum, current_running_sum)  # update max
            current_running_sum -= arr[i - (k-1)]  # shrink window
    return max_sum


if __name__ == "__main__":
    print("Find maximum sum of subarray of size K")
    arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    k = 3
    print(find_max_sum_subarray(arr, k))

