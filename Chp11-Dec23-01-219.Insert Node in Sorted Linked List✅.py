class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The head of Linked List
    @param val: An Integer
    @return: The head of new Linked List

    # 🎯 understand what are conventions of writing @parameter, @return
    """

    def insertNode(self, head, val):  # head = 1->4->6->null ; val = 5
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
