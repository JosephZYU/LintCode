class TreeNode:
    def __init__(self, val):
        self.left, self.right = None, None


class Solution:

    def add_to_lists(self, lists, curr_level, value):
        # PENDING INPUT

    def dfs(self, node, lists):
        # 递归的出口/终点
        if node is None:
            # 返回-1，使父节点（叶子节点）的level为0
            return -1

        # 递归的拆解 left, right
        left_level = self.dfs(node.left, lists)
        right_level = self.dfs(node.right, lists)

        # 拆解完后，合并
        curr_level = max(left_level, right_level) + 1

        self.add_to_lists(lists, curr_level, node.val)

        return curr_level

    def findLevase(self, root):

        lists = []

        # 异常检测
        if root is None:
            return lists

        # 使用了后序遍历，先处理1左和2右，最后处理3根节点

        # 使用DFS
        self.dfs(root, lists)
        return lists
