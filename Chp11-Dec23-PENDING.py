"""
Create dummy point, dummy.next = head

Features of dummy point:

    1. dummy.next always point to the "updated" list head
    2. easy of handling edge cases
"""


class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False


def insertNode(head, value):
    dummy = ListNode(float('-inf'))
    dummy.next = head
    curr_node = dummy

    while curr_node.next and curr_node.next.val <= value:
        curr_node = curr_node.next

    new_node = ListNode(value)
    new_node.next = curr_node.next
    curr_node.next = new_node

    return dummy.next
