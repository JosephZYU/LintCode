"""
Linked List 单链 ⛓️

A single "Touch Point" is a Node - which is an independent class by itself!

The very 1st Node = head Node

Every Node has two properties:
    1. val (value 节点值)
    2. next (next 下一个节点的引用)

Basic methods of Linked List:
    1. head = head.next （指针后移)
    2. head.next = anotherNode (改变Node对应的Next; E.g. head.next = head.next.next)
       tips: you can save head.next into "ex-variable" before breaking up (link to the anotherNode)


Questions:

    1. 增加节点 - insert Node in a sorted list✅
    2. 删除节点 - remove linked list element✅
    3. 交换节点 - swap two nodes in a linked list
    4. 寻找中点 - (locate) middle of the linked list (😎 make sure to clearify 中间偏左 或 偏右)✅
    5. 旋转列表 - rotate list （🧠 think of Roman legion on the battle field）✅
    6. 反转列表 - reorder list (complete reverse the list order)
    7. 合并列表 - reorder list
    8. 循环列表 - insert into a cyclic sorted list (cyclical list)
"""

# 🎯 do we have to put 'object' inside the class ()?
# Everything from the __init__ are "intrinsic values"


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
