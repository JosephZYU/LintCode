# Ref - https://youtu.be/WwfhLC16bis

class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Manually create: 6 -> 3 -> 4 -> 2 -> 1 -> None

node_head = ListNode(6)
node_b = ListNode(3)
node_c = ListNode(4)
node_d = ListNode(2)
node_e = ListNode(1)

node_head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e


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


def print_linkedlist(node_head):
    while True:
        print(node_head.value, '-> ', end='')

        if node_head.next is None:
            # if not node_head.next:
            print('None')
            break

        node_head = node_head.next


print_linkedlist(node_head)


# while True:
#     print(node_head.value, '-> ', end='')

#     if node_head.next is None:
#         # if not node_head.next:
#         print('None')
#         break

#     node_head = node_head.next
