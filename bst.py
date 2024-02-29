class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

seventeen = BinaryNode(17)
twelve = BinaryNode(12)
twenty = BinaryNode(20, seventeen);
fifteen = BinaryNode(15, twelve, twenty)
four = BinaryNode(4)
eight = BinaryNode(8, four)
root = BinaryNode(10, eight, fifteen)

#PreOrder Traversal

def preorder_traversal(node):
    if node is None:
        return

    print(node)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

#InOrder Traversal

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node)
    inorder_traversal(node.right)

#PostOrder Traversal
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node)

preorder_traversal(root)
inorder_traversal(root)
postorder_traversal(root)

from collections import deque

def preorder_iterative(root):
    s = deque()
    s.append(root)
    while len(s) > 0:
        current = s.pop()
        print(current)
        if current.right is not None:
            s.append(current.right)
        if current.left is not None:
            s.append(current.left)

preorder_iterative(root)
