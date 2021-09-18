"""
SITUATION
1. Listen and read problem and examples/ Repeat in own words
    Given an array with positive numbers and a positive target number,
    find all of its contiguous subarrays whose product is less than the target
    number.
    ex. [2, 5, 3, 10], target=30  -> [2], [5], [2, 5], [3], [5, 3], [10]
2. Confirm in/out, ask clarifying questions.
    in: arr w/ pos int, pos target
    out: 2d array containing valid subarrays

TASK
1. Think out loud, diagram
    [2, 5, 3, 10], target=30
   p1/p2
    [2, 5, 3, 10], target=30  [ ]

    When p1 and p2 are at the same index, check if condition is satisfied.
    If yes, append the value to its own list and extend it to the 2d list.
    If its not, move p1

"""


def find_products_below_target(arr, target):
    # while p1 less than len of array



if __name__ == '__main__':
    print("Subarrays with Product Less than a Target")
