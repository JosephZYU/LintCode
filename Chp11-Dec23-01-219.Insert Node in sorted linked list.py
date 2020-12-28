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



Questions:

    1. 增加节点 - ✅insert Node in a sorted list
    2. 删除节点 - ✅remove linked list element
    3. 交换节点 - swap two nodes in a linked list
    4. 寻找中点 - ✅(locate) middle of the linked list (😎 make sure to clearify 中间偏左 或 偏右)
    5. 旋转列表 - ✅rotate list （🧠 think of Roman legion on the battle field）
    6. 反转列表 - reorder list (complete reverse the list order)
    7. 合并列表 - reorder list
    8. 循环列表 - insert into a cyclic sorted list (cyclical list)


"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insertNode(head, val):
    """ create a NEW dummy node """

    # 🎯 What is float('-inf') 最小整数值?
    dummy = ListNode(float('-inf'))
    dummy.next = head
    curr_node = dummy

    """ 同时满足： 下一个点为真是存在的节点 & 下一个节点的值小于目标值 """
    """ while 循环的本质： 其实是traverse， 遍历各个节点"""

    while curr_node.next and curr_node.next.val <= val:
        curr_node = curr_node.next

    """ insert New Node """
    new_node = ListNode(val)  # create new node based on ListNode()
    new_node.next = curr_node.next  # break the old chain & assign the new chain
    curr_node.next = new_node  # finally: link the current node with the new node

    return dummy.next


a = ListNode([1, 4, 6], 5)

print(a)
