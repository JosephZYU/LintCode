# Ref - https://stackabuse.com/python-linked-lists/
# Remove ALL elements from a linked list of integers that have value (val)

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):

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
