#Trees
class Node:
  def __init__(self,data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self,child):
    child.parent = self
    self.children.append(child)

  def get_level(self): #this tells the level of the node
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
      
    return level

  def print_tree(self):
    spaces = ' ' * self.get_level() * 3 # prints the 3 spaces acc to levels
    prefix = spaces + "|__" if self.parent else ""

    print(prefix + self.data) # Prints the current node data
    # Now print the children data

    if len(self.children) > 0 : # or if self.children (if leaf node then dont execute)
      for child in self.children:
        # print(child.data) 
        # above prints the data of children of only the parent. wt abt the children of each child node
        
        # since child is an object of Node class and Node class has a printtree method we recursively call it to solve above prob
        child.print_tree()


def build_product_tree():
  root = Node("Electronics")

  laptop = Node("laptop")
  laptop.add_child(Node("mac"))
  laptop.add_child(Node("win"))
  laptop.add_child(Node("linux"))

  tv = Node("tv")
  tv.add_child(Node("mac"))
  tv.add_child(Node("win"))
  tv.add_child(Node("linux"))
  
  root.add_child(laptop)
  root.add_child(tv)

  # print(tv.get_level()) # 1
  return root

if __name__ == '__main__':
  root = build_product_tree()
  # print(root.get_level()) # 0
  root.print_tree()
  pass