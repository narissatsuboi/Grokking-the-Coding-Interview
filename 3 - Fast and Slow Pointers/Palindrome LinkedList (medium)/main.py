"""
Given the head of a Singly LinkedList, write a method to check if the
LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should
be in the original form once the algorithm is finished. The algorithm should
have O(N) time complexity where ‘N’ is the number of nodes in the
LinkedList.
"""

import unittest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Support Functions
# Find Middle
# Reverse
# Print List


def find_middle(node):
    """
    Uses slow and fast pointers to find middle of linked list.
    Advance fast pointer 2x as fast as slow pointer. When fast reaches
    the end of the list, slow is pointing to the middle.
    O(n) time | O(1) space
    :param head: start of search for middle
    :return: node representing middle
    """
    slow, fast = node, node
    while fast is not None and fast.next is not None:
        slow = slow.next  # 1 pace
        fast = fast.next.next  # 2 paces
    return slow


def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head

    prev = None
    while head is not None:
        next = head.next  # store where head is pointing to b4 reversal
        head.next = prev  # reverse head's pointer
        prev = head  # move prev pointer over to where head is
        head = next  # move head to the stored next location
    return prev  # new head


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end='->')
        current = current.next


def is_palindrome(head):
    """
    Story: given a singly linked list, determine if the nodes create a
    palindrome in constant space and returning the linkedlist the same.
    Input: Head of linked list
    Output: True if palindrome
    Approach:
    If palindrome, the first half of the list is the reverse of the second
    half of the list. Slow and fast pointers. O(n) space | O(1) time.
    :param head:
    :return: True if palindrome
    """
    # 1 Find middle of list
    mid_node = find_middle(head)
    # 2 When middle is found, reverse the second half of the list
    head_second_half = reverse(mid_node)
    # 3 Store head to second half so we can undo the reverse later since the
    # problem requires us to return the list in original order
    copy_head_second_half = head_second_half
    # 4 Compare each element in the list with the node value while they match.
    # If they match until null -> True.
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break  # not palindrome, will return False
        else:  # continue traversals
            head = head.next
            head_second_half = head_second_half.next
    # 5 we have to reverse the linked list back before we return anything
    reverse(copy_head_second_half)  # undo step 2
    # 6 Catch palindrome condition
    if head is None or head_second_half is None:
        return True
    return False


class TestPalindromeLinkedList(unittest.TestCase):

    def test_find_middle(self):
        head = ListNode(2)
        head.next = ListNode(4)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(1)
        self.assertEqual(head.next.next, find_middle(head))

    def test_reverse(self):
        head = ListNode(2)
        head.next = ListNode(4)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(1)
        print_list(head)
        print()
        rev_head = reverse(head)
        print_list(rev_head)
        print()

    def test_is_palindrome(self):
        head = ListNode(2)
        head.next = ListNode(4)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(2)
        self.assertTrue(is_palindrome(head))
        head = ListNode(2)
        head.next = ListNode(4)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(1)
        self.assertFalse(is_palindrome(head))
        head = None
        self.assertTrue(is_palindrome(head))


if __name__ == '__main__':

    unittest.main(verbosity=2)



