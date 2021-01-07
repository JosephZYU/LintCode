class LinedListNode:
    # 首先，需要自建链表节点
    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:

    def __init__(self):
        # 本身没有意义，为了保存头节点的引用
        self.before_head = LinedListNode(-1)
        # 初始时队列为空的
        self.tail = self.before_head

    # 入队
    def enqueue(self, item):
        # 新建一个节点，用tail指向它 -> 代表了新节点入队
        self.tail.next = LinedListNode(item)
        # 跟新队尾
        self.tail = self.tail.next

    # 出队
    def dequeue(self):
        # 判空
        if self.before_head.next is None:
            return -1

        # 保存头节点的值
        head_val = self.before_head.next.val

        # 以跳过代替删除
        self.before_head = self.before_head.next

        return head_val
