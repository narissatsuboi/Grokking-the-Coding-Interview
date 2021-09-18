"""
Given the head of a Singly LinkedList that CONTAINS a cycle, write a
function to find the starting node of the cycle.

Clarifying - CLL could be at the start of the list? Duplicate elements in
the list?
Input - CLL with cycle.
Output - Starting node of cycle.

Approach.
1. Point slow and fast pointers to head
2. Find length of cll - K
3. Move fast ahead by K nodes
4. Increment slow and fast by 1 until they meet
5. Meeting point is at the start of the cycle
"""

# Node Structure
class Node:
    # Initialize a Node with data
    def __init__(self, data):
        self.data = data
        self.next = None

def find_start_cll(head):
    cycle_length = 0
    # find the cll cycle
    slow, fast =
    while fast is None and fast.next is not None:


# Find start CLL helper function
def calc_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


# Given the length of the cycle, return the starting node of the cycle
def find_cll_start(head, cycle_length):
    slow, fast = head, head
    # move fast pointer ahead "cyle length" nodes
    while cycle_length > 0:
        fast = fast.next
        cycle_length -= 1
    # increment both until they meet
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == '__main__':

