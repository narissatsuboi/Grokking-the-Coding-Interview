"""
Given an array of characters where each character represents a fruit tree,
you are given two baskets, and your goal is to put maximum number of fruits
in each basket. The only restriction is that each basket can have only one
type of fruit.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick one fruit from each tree until you cannot, i.e., you will stop
when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.
"""

import unittest

def fruit_into_baskets(fruits):
    window_start, max_length = 0, 0
    fruit_frequency = {}

    for window_end in range(len(fruits)):
        # add next fruit to hashmap
        right_fruit = fruits[window_end]

        # reset frequency hash map to 0 if character not in map
        # this means there are no instances of this character
        # in the current sliding window
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # limiting condition
        while len(fruit_frequency) > 2:
            # decrement the frequency of the char at window start
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1

            # when the character's frequency is 0, delete it from the hashmap
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]

            # shrink the bound of the window by incrementing window start
            window_start += 1

        # store max_length
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


class TestFruitIntoBaskets(unittest.TestCase):
    def test_fruit_into_baskets(self):
        self.assertEqual(3, fruit_into_baskets(['A', 'B', 'C', 'A', 'C']))
        self.assertEqual(5, fruit_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Fruit in Baskets")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
