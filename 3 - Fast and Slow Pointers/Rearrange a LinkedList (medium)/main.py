"""
Given the head of a Singly LinkedList, write a function
to determine if the LinkedList has a cycle in it or not.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    """
    Understand the Problem: Given the start of sll, figure out if the list
    has a cycle somewhere in it. A cycle occurs when the same number is
    traversed more than once, and None is never reached.
    Clarify: We may receive an empty list, which can be easily handled.
    Approach: We can use a fast pointer to advance ahead of the slow
    pointer.
        If there IS a cycle, eventually the fast pointer will overlap
        with the slow pointer.
        If there ISNT a cycle, the fast pointer will reach null.
    :param head: start of sll.
    :return: True if cycle in slll.
    """





if __name__ == '__main__':
    print("Find the Cycle")
