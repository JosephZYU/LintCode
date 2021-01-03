# Find the Middle of linked list
# NOTE: 默认偶数时，为中间偏右
# 0:20:38"

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # 1:34:30" Line 14 - 26
    def middleNode(self, head):

        # 🧠 fix-memory
        # Handle special case first!
        if head is None:
            return None

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
