"""
Tree = [1, 2, 3, 4, 5, 6, 7]

       1
   2       3
 4   5   6   7
N N N N N N N N 

Pro-order 前序遍历:  1, 2, 4, 5, 3, 6, 7 (撞南墙才回头！)

In-order 中序遍历:   4, 2, 5, 1, 6, 3, 7

Post-order 后序遍历: 4, 5, 2, 6, 7, 3, 1


Input: {1, 2, 3, 4, 5, #, #}

       1
   2       3
 4   5   N   N
N N N N 

Output: [[4, 5, 3], [2], [1]]

"""
# https://www.jiuzhang.com/course/84/dialog/#chapter-468_1
# 🎯🎯🎯 [Start Time] - [02:24:53"]


class Solution:
    # 主函数：初始化一个结果集，返回一个结果集
    # 进行一次DFS(深度优先搜索🔍) NOTE：此处DFS为后根遍历
    def findLeaves(self, root):
        lists = []
        self.dfs(root, lists)
        return lists

    # DFS为后根遍历，先左孩子，再右孩子，最后父亲
    def dfs(self, node, lists):
        if node is None:
            # 返回-1很巧妙，对于根节点4而言，父亲节点+1后变为0层
            return -1

        # 通过不断的递归调用，求出左边和右边两侧的值
        left_level = self.dfs(node.left, lists)  # -1
        right_level = self.dfs(node.right, lists)  # -1

        # 当前level = 左右孩子level的最大值 + 1
        curr_level = max(left_level, right_level) + 1

        # 将当前节点的值，通过一个新的func，放入它属于的那一层
        # (将之插入到“结果集”中，对应的那一层 E.g. [4, 5, 3] 同属一层)
        self.add_into_lists(lists, curr_level, node.val)

    # 把某个节点的值，加入某一层
    def add_into_lists(self, lists, level, value):
        # 如果lists还没有第level层，加入一层
        # if level:0 == len(lists):0 -> 刚层不存在，需要建立新一层
        if level == len(lists):
            lists.append([])
        lists[level].append(value)
