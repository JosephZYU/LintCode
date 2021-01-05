"""
Input: {3, 9, 20, #, #, 15, 7}
Output: [[3], [20, 9], [15, 7]]

Ref - https://www.jiuzhang.com/course/84/dialog/#chapter-468_1 - @ 1:00:35"
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def zigzagLeveOrder(root: TreeNode):
    # 创建空列表，作为最终输出
    lists = []

    # 特殊情况处理
    if not root:
        return lists

    # 准备: 创建两个stacks，建立方向标记
    stack = []
    next_stack = []
    stack.append(root)
    is_left_to_right = True

    # 开始循环
    while len(stack) != 0:
        # 存放当前层的所有Nodes
        l = []

        # 取出当前stack内的所有Node
        while len(stack) != 0:
            curr_node = stack.pop()

            # 如果Node为空(None), 不做任何处理，直接continue
            if not curr_node:
                continue

            # 置换操作 1 of 2 (父节点存入输出结果): 当前Node，进入当前层l暂放
            l.append(curr_node.val)

            # 置换操作 2 of 2 (对应子节点存入下一个Stack): 将当前Node对应的子节点，放入next_stack
            # 同时，需要先判断是否为从左往右

            if is_left_to_right:
                next_stack.append(curr_node.left)
                next_stack.append(curr_node.right)
            else:
                next_stack.append(curr_node.right)
                next_stack.append(curr_node.left)

        # 翻转方向
        is_left_to_right = not is_left_to_right

        # NOTE: l必须存在东西，才加入lists (l可能为kong，当前层全部是None)
        if len(l) > 0:
            lists.append(l)

        # 交换Stack
        stack, next_stack = next_stack, stack

    return lists
