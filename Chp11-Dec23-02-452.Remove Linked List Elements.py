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


"""class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next"""

"""def removeElements(head, value):
    dummy = ListNode(0)
    dummy.next = head
    head = dummy

    while head.next:
        if head.next.val == value:
            head.next = head.next.next
        else:

            head = head.next

    return dummy.next"""

# ⏭ 所谓的指针 -> head

"""def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    head = dummy

    while dummy.next:
        if dummy.next.val == val:
            dummy.next = dummy.next.next
        else:
            head = head.next

    return dummy.next"""


def removeElements(head, val):

    dummy = ListNode(0)
    dummy.next = head
    head = dummy

    while head.next:
        # 如果指针的下一个点为val，跳过
        if head.next.val == val:
            head.next = head.next.next
        # 指针后移
        else:
            head = head.next

    return dummy.next
