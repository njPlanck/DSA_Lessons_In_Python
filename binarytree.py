class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None




class Tree():
  def __init__(self, root):
    self.root = Node(root)


  def preorder(self,start,records):
    if start is not None:
      records.append(start.value)


tree = Tree(5)

tree.root.right = Node(4)
tree.root.left = Node(3)


print(tree.root.value)