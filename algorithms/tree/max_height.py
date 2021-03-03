"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""

# def max_height(root):
#     if not root:
#         return 0
#     return max(maxDepth(root.left), maxDepth(root.right)) + 1

# iterative


def max_height(root):
    if root is None:
        return 0
    height = 0
    queue = [root]
    while queue:
        height += 1
        level = []
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)
        queue = level
    return height

