#Binary treelerde inorder, postorder ve preorder sıralanışlarını yazdıran fonksiyonlar modülü.

#Tree'nin her nodunu "Node object" olarak kaydederek treeyi aklımda tutuyorum adjacency list şeklinde.
class Node:
    def __init__(self, key):
        #self.a = "instance attribute" -- bu ne ben de bilmiyorum o yüzden yoruma attım boş bir şey herhalde.:D
        self.left = None
        self.right = None
        self.val = key
        

def inorder(root):
    if root:
        ınorder(root.left)
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


