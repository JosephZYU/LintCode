# https://youtu.be/Ast5sKQXxEU
# https://github.com/joeyajames/Python/blob/master/LinkedLists/LinkedList0.py

class Node(object):

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList (object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None


myList = LinkedList()


myList.add(1)
myList.add(4)
myList.add(7)

print(myList)
print("size="+str(myList.get_size()))

print(myList.find(1))
print(myList.find(4))
print(myList.find(6))


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Resume from 0:54:50 ~ 1:02:10

    """
    @param head: The head of Linked List
    @param val: An Integer
    @return: The head of new Linked List

    # 🎯 understand what are conventions of writing @parameter, @return
    """


def insertNode(head, val):  # head = 1->4->6->null ; val = 5
    # 创建dummy点，dummy.next = head
    # dummy点的作用：
    # 1.1. dummy.next永远指向处理过后的链表的表头
    # 1.2. 方便处理初始值为Null的特殊情况

    # 创建“当前所在的指针” curr_node, 让curr_node指向新创建的dummy node

    # 🎯 verify if float('-inf') or float('inf') -> 最小值？

    dummy = ListNode(float('-inf'))
    dummy.next = head
    curr_node = dummy

    # 2.1. 判断下一个节点真是存在 (判断是否已经到末尾了)
    # 2.2. 同时，下一个节点的值小于（小于等于）目标值的时候：
    # -> 将当前指针后移一位. 直到下一节点的值大于目标值为止
    while curr_node.next and curr_node.next.val < val:
        curr_node = curr_node.next

    # 3.1. 创建新节点
    # 3.2. 插入新节点
    # 😎 对于linked list，遵守“先顾后，再接前”的原则，确保链接顺利
    new_node = ListNode(val)  # val = 5
    new_node.next = curr_node.next  # 😎 symmetric
    curr_node.next = new_node

    # 4. 输出从dummy点之后开始的完整链表 # 1->4->5->6->null
    return dummy.next


print(insertNode(myList, 5))
