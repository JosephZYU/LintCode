"""
linked list

head node -> next node -> next node -> end node

🧠 node = val + next

Every node consist of:

    1. val: string, integer, ...

    2. self.next: ⏭ 


Basic Methods:

    1. 指针后移 head = head.next

    2. head.next = anotherNode; 一旦完成，再也找不回原来的 head.next (save head.next as "")

    3. 

"""


"""class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
