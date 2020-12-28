# Find the Middle of linked list


# 0:20:38"

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # 1:34:30"
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
