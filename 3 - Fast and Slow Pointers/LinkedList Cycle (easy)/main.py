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
    Clarify: We may receive an empty list, which can be easily handled. An
    empty list is not cyclical.
    Approach: We can use a fast pointer to advance ahead of the slow
    pointer.
        If there IS a cycle, eventually the fast pointer will overlap
        with the slow pointer.
        If there ISNT a cycle, the fast pointer will reach null.
    :param head: start of sll.
    :return: True if cycle in slll.
    """
    # handle empty list
    if head is None or head.next is None:
        return True

    # pointer init
    slow, fast = head, head  # point both to start of list

    # advance pointers in while loop
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # check for cycle condition
        if slow == fast:
            return True

    return False  # fast reached None, not cycle


if __name__ == '__main__':
    print("Find the Cycle")
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))