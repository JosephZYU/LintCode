

# Definition of ListNode:

class listNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def insertNode(self, head, val):


def insertNode(head, val):

    # Create fake dummy
    dummy = listNode(float('inf'))

    # Deal with extreme case
    dummy.next = head

    # Find/locate position
    curr_node = dummy

    # 🎯 understand why it can be <= or <
    # 1 of 2: test if there still is a 'next' node exists
    # 2 of 2: determine the next.val compared to target value
    while curr_node.next and curr_node.next.val <= val:
        curr_node = curr_node.next

    # Create the 'New' node
    new_node = listNode(val)

    # 1 of 2: Link 'New' node point to the current next
    new_node.next = curr_node.next

    # 2 of 2: Link current node to the 'New' node
    curr_node.next = new_node

    return dummy.next


insertNode(1, 4)
