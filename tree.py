class Node:
    #a = 10
    def __init__(self, key):
        #self.a = "instance attribute" -- bu ne ben de bilmiyorum :D
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root:
        ınorder(root.left) # indorder(7) > indorder(3) > inorder(2) > inorder(?)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


