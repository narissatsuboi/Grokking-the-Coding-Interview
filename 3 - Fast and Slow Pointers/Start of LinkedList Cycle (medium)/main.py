"""
Given the head of a Singly LinkedList that CONTAINS a cycle, write a
function to find the starting node of the cycle.

Clarifying - CLL could be at the start of the list? Duplicate elements in
the list?
Input - CLL with cycle.
Output - Starting node of cycle.

1. Find cycle length
2. Find cycle start node
"""


# Node Structure
class Node:
    # Initialize a Node with data
    def __init__(self, data):
        self.data = data
        self.next = None


"""
How to find cycle length
1. Find the node where a slow and fast pointer overlap. 
2. From that node, traverse the cycle until the traversal pointer is at the 
starting point. 
"""


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        # check for overlap, pass node to helper
        if slow == fast:
            cycle_len = find_cycle_length_helper(slow)
            break
    return find_cycle_start(head, cycle_len)


def find_cycle_length_helper(slow):
    curr = slow
    cycle_len = 0  # accumulator
    while True:
        curr = curr.next
        cycle_len = cycle_len.next
        if curr == slow:
            break
    return cycle_len


"""
How to find the start of the cycle
1. Given the length of the cycle, place two pointers at head and move the 
fast pointer K nodes forward. 
2. Increment slow and fast one time each iteration until they overlap.
3. Return that node. 
"""


def find_cycle_start(head, cycle_len):
    slow, fast = head, head
    for i in cycle_len:
        fast = fast.next
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == '__main__':
    print("test")

