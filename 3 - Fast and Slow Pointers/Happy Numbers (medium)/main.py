"""
Any number will be called a happy number if, after repeatedly replacing it
with a number equal to the sum of the square of all of its digits, leads us
to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
they will be stuck in a cycle of numbers which does not include ‘1’.

Input: Pos or neg integer
Output: True if happy
Story: given an integer, find out if the sum of its squares is happy,
if not calculate the sum of its squares. When is an integer NOT happy? When
the same number is encountered twice, then we're inside a cycle.
Approach:
 - Hashmap to track the occurrences of the numbers. O(n) time | bad space
 - LinkedList to ID a ll cycle. O(n) time | bad space for large N too.
 - * Variables hold slow and fast square sums. When their values overlap,
 a duplicate square sum has been reached. Else, its reached 1.
"""

import unittest

# Steps
# 1. Calculate the square of the sums for pos/neg numbers
# 2. Assign to slow and fast pointers
# 3. Repeat until nums are the same.
# 4. If never the same, happy number!


def square_sums(num):
    """
    :param num: function will disregard numbers < 0.
    :return: number representing the sum of the square of the digits in the num
    """
    sum_square_digits = 0  # accumulator for sum of the sq of all digits in num
    while num > 0:  # diminish num one digit at a time
        digit = num % 10  # mod 10 to get the digit
        sum_square_digits = digit * digit  # add the sq of the digits
        num //= 10
    return sum_square_digits


def find_happy_number(num):
    slow, fast = num, num
    print("Num=", num, end=' ')
    while True:
        slow = square_sums(slow)
        fast = square_sums(square_sums(fast))
        print(slow, fast, "->", end='')
        if slow == fast:
            break
    print()
    return slow == 1


class TestHappyNumbers(unittest.TestCase):
    def test_find_happy_number(self):
        self.assertEqual(False, find_happy_number(0))
        self.assertEqual(True, find_happy_number(1))
        self.assertEqual(True, find_happy_number(23))
        self.assertEqual(True, find_happy_number(2))
        self.assertEqual(True, find_happy_number(24))


if __name__ == '__main__':
    print("Happy Numbers")
    # print(find_happy_number(23))
    unittest.main(verbosity=2)