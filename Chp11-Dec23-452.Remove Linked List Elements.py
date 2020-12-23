# Ref - https://stackabuse.com/python-linked-lists/

# Remove ALL elements from a linked list of integers that have value (val)

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


def removeElements(head, value):
    dummy = ListNode(0)
    dummy.next = head
    head = dummy

    while head.next:
        if head.next.val == value:
            head.next = head.next.next
        else:

            head = head.next

    return dummy.next
