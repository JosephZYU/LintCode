"""
Input: {1, 2, 3}
Output: [[1], [3, 2]]

奇数层从左往右，偶数层从右往左

Ref - https://www.jiuzhang.com/course/84/dialog/#chapter-400_2

"""

# Definition of TreeNode
# 🎯 But why it has to be None?
# 🧐 Isn't it supposed to be something instead of None?
# 🧐 Or can we -> __init__(self, val, left=None, right=None)?


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def zigzagLevelOrder(root):
    # 整体性的结果，本质为Queue
    lists = []

    # 异常检测
    if not root:
        return lists

    # 逐层循环：使用两个stack，交替存放Nodes
    # 适用两个stack迭代，逐层拓展的循环！
    # NOTE：对于需要“交替翻转”的题型，非常适用stack！
    stack = []
    next_stack = []

    stack.append(root)

    # 标记：当前层的Node存放顺序是否为 - 从左往右
    is_left_to_right = True

    # 正式启动BFS循环
    # 只要当前层非空(长度不为零)
    while len(stack) != 0:
        # 记录当前层的Node
        nodes = []

        # 处理这一层：取出当前层的所有Nodes，并扩展下一层放进next_stack
        while len(stack) != 0:
            # 弹出一个Node (取出并pop扔掉)
            curr_node = stack.pop()

            # 如果当前节点为空，则不做任何处理
            # 🧠 continue -> Do Nothing!
            if curr_node is None:
                continue

            # 如果不是None，则可能拓展left和right两个子节点
            nodes.append(curr_node.val)

            # 判断当前层的遍历方向，如果为从左往右：
            if is_left_to_right:
                next_stack.append(curr_node.left)
                next_stack.append(curr_node.right)

            else:
                next_stack.append(curr_node.right)
                next_stack.append(curr_node.left)

        # 处理下一层：
        # 首先必须翻转方向 🔄
        is_left_to_right = not is_left_to_right

        # Nodes不是空的list
        if len(nodes) > 0:
            lists.append(nodes)

        # 将两个stack交换 - stack的迭代
        stack = next_stack
        next_stack = []

    return lists
