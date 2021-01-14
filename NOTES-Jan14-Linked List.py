
# Definition of ListNode

"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# ✅ how to visually present/print the linked list E.g. 6 -> 3 -> 4 -> 2 -> 1

class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


node_head = ListNode(6)
node_b = ListNode(3)
node_c = ListNode(4)
node_d = ListNode(2)
node_e = ListNode(1)

node_head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e

# ✅ Simple Ways To Code Linked Lists In Python
# Ref - https://youtu.be/6sBsF13n5ig?t=290


# while True:
#     print(node_head.value, '-> ', end='')

#     if node_head.next is None:
#         # if not node_head.next:
#         print('None')
#         break

#     node_head = node_head.next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):

        # Create node from class ListNode above
        node = ListNode(value)

        # Edge case
        if self.head is None:
            self.head = node
            return

        # Define our current node as our head node
        curr_node = self.head

        # Traverse the ENTIRE linked list
        while True:
            if curr_node.next is None:
                curr_node.next = node
                break
            curr_node = curr_node.next

    def print_linkedlist(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value, '-> ', end='')
            curr_node = curr_node.next
        print('None')


"""

# Ref - https://youtu.be/WwfhLC16bis

def count_nodes(node):

    # Create number of count
    count = 0

    # Edge case
    if not node:
        return count

    # if node exist and node.next exist -> move to the next node
    while node and node.next:
        count += 1
        node = node.next

    return count + 1


print(count_nodes(node_head))

print(node_head)
"""
