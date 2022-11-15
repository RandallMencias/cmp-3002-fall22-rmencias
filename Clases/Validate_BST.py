

def bst(node, low, high):
    if (not node.left) and (not node.right):
        return True
    if node <= low or node >= high:
        return False
    return (node.left, low, node.val) and (node.right, node.val, high)
