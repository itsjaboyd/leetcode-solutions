import typing
from typing import Optional

# Problem 2: https://leetcode.com/problems/add-two-numbers/

# Intuition


# Since the linked lists are already given to us reversed, we can simply add up
# each digit and carry over onto the next, which will give us the reversed
# result.

# Approach

# For each node element in both lists, add the value. If it happens to be larger
# then 10, then carry this value over to the next node operation. If both nodes
# are empty and there is no carry, then break out of the loop traversing both
# linked lists.

# Time complexity

# Since building the resulting linked list only requires traversing both lists,
# the time complexity is O(n), where n is the length of the loger list of the
# two.

# Space complexity

# Building the additions from each node of the two lists requires n digits of
# space, therefore the space complexity of the algorithm is O(n).


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({str(self.val)})"


def addTwoNumbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    result = ListNode()
    head = result
    carry = False
    while True:
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0
        current = l1_value + l2_value
        current += 1 if carry else 0

        result.val = current % 10
        carry = True if current >= 10 else False

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

        if l1 is None and l2 is None and not carry:
            break

        result.next = ListNode()
        result = result.next
    return head


def printListNode(node_list: Optional[ListNode]) -> None:
    values = []
    while node_list is not None:
        values.append(node_list.val)
        node_list = node_list.next

    values = [str(value) for value in values]
    print(" -> ".join(values))


def main():
    n2 = ListNode(3)
    n1 = ListNode(4, n2)
    l1 = ListNode(2, n1)

    n2 = ListNode(4)
    n1 = ListNode(6, n2)
    l2 = ListNode(5, n1)

    printListNode(l1)
    printListNode(l2)

    result = addTwoNumbers(l1, l2)
    print("Result:")
    printListNode(result)


if __name__ == "__main__":
    main()
