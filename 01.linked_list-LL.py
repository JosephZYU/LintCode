# Ref - https://youtu.be/6sBsF13n5ig


class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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


ll = LinkedList()

ll.print_linkedlist()

ll.insert(33)
ll.print_linkedlist()

ll.insert(44)
ll.print_linkedlist()

ll.insert(55)
ll.print_linkedlist()
