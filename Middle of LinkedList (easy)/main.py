"""
Given the head of a Singly LinkedList, write a method to return the middle
node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second
middle node.

Story: Given a LL return middle node, or the second middle node if the len
of the list is even.
Input: LL head. Output: Node.
Approaches:
- BF - Traverse len of LL once to get n, traverse to n/2 and return none. O(
n + n/2) time | O(1) space
- Slow and fast pointers, keep fast pointer double the nodes ahead of slow.
When fast pointer is null, slow pointer is at middle node. Single traversal,
O(n) | O(1) space.
"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_node(head):
    slow, fast = head, head  # start pointers at same spot

    # advance pointers until fast's next points to null
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    print("Middle of LinkedList")
