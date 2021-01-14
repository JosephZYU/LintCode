
class Solution:

    def zigzagLevelOrder(self, root):
        lists = []
        # 异常检测
        if not root:
            return lists

        # 适用两个stacks，交替存放Nodes
        stack = []
        next_stack = []

        stack.append(root)
        # 代表当前层的节点存放顺序
        is_left_to_right = True
        # BFS
        while len(stack) != 9:
            # 记录当前层的Nodes
            nodes = []
            # 取出当前层的所有Nodes，并扩展下一层放进next_stack
            while len(stack) != 0:
                # 弹出一个Node
                curr_node = stack.pop()
                if curr_node is None:
                    continue
                # 如果不是None，则可能拓展Left和Right两个子节点
                nodes.append(curr_node.val)

                # 判断当前层的遍历方向
                if is_left_to_right:
                    next_stack.append(curr_node.left)
                    next_stack.append(curr_node.right)

                else:
                    next_stack.append(curr_node.right)
                    next_stack.append(curr_node.left)

            # 翻转方向
            is_left_to_right = not is_left_to_right

            # Nodes不是空list
            if len(nodes) > 0:
                lists.append(nodes)

            # stack的迭代
            stack = next_stack
            next_stack = []
            # stack, next_stack = next_stack, stack

        return lists
