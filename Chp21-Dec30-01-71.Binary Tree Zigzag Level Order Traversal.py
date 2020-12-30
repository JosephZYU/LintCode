"""
Given a binary tree, return the zigzag level order traversal of its nodes' value

from left to right, then right to left for the next level and alternate between.

"""


def zigzagLevelOrder(self, root: TreeNode):
    lists = []

    # 如果为空数，直接返回
    if not root:
        return lists

    # BFS要用到队列
    q = collections.deque()

    # 正方向标记
    is_left_to_right = True
    q.append(root)

    while len(q) != 0:
        size = len(q)
        l = []
        for i in range(size):
            node = q.popleft()
            l.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not is_left_to_right:
            l.reverse()

        lists.append(l)

        is_left_to_right = not is_left_to_right

    return lists
