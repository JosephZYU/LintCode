"""
NOTE: Don't be afraid!

1.No matter how we "define" the pay should be, it does NOT force the input to be integer or float
2.Likewise, '->' doesn't force anything either. They simply indicate to the programmer the ideal input


Ref - https://stackoverflow.com/a/56002484

"""

"""
class Robot:
    # 👀 ALWAYS remember to put 'self' to indicate they all belong to the same class
    # __init__: constructor
    def __init__(self, first, last, pay: float):
        self.first = first
        self.last = last
        self.pay = pay

    def introduce_self(self):
        print(f'Hello! My name is {self.first} {self.last}\n{self.abbre}')

    def show_payment(self) -> int:
        return int(self.pay)


a = Robot('Joseph', 'Yu', 5.456)

# YES - we can define stand-alone attribute to be stored into class
a.abbre = 'JYU'

print(a.show_payment())
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def insertionSortList(self, head):
        dummy = ListNode()
        curr = head

    # def insertionSortList(self, head: ListNode) -> ListNode:
    #     dummy = ListNode()
    #     curr = head

        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy

            # find the position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

        return dummy.next


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee('Joseph', 'Yu', 60000).fullname())
