

def min_depth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    if root.left is not None or root.right is not None:
        return max(self.minDepth(root.left), self.minDepth(root.right))+1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# iterative
def min_height(root):
    if root is None:
        return 0
    height = 0
    level = [root]
    while level:
        height += 1
        new_level = []
        for node in level:
            if node.left is None and node.right is None:
                return height
            if node.left is not None:
                new_level.append(node.left)
            if node.right is not None:
                new_level.append(node.right)
        level = new_level
    return height
