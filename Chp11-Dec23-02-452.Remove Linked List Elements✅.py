# Ref - https://stackabuse.com/python-linked-lists/
# Remove ALL elements from a linked list of integers that have value (val)

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 3 -> null
# 1 -> 2 -> 4 -> 5 -> null


class Solution:
    """
    @param head: a ListNode
    @param val: an integer
    @return: a ListNode
    """

    def removeElements(self, head, val):

        dummy = ListNode(0)
        dummy.next = head
        curr_node = dummy

        while curr_node.next:
            # 如果指针的下一个点为val，跳过(Delete)
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            # 指针后移
            else:
                curr_node = curr_node.next

        return dummy.next
