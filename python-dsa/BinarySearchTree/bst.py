from typing import Union

class TreeNode:
    left: Union["None", "TreeNode"]
    right: Union["None", "TreeNode"]
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

def checkbst(node, min_value = float('-inf'), max_value = float('inf')):
     if node is None :
         return True
     if not min_value < node.key < max_value :
         return False
     return checkbst(node.left,min_value,node.key) and checkbst(node.right, node.key, max_value)


def makeTree(data):
    if data is None:
        return None
    elif isinstance(data, tuple) and len(data) == 3 :
        node = TreeNode(data[1])
        node.left = makeTree(data[0])
        node.right = makeTree(data[2])
    elif isinstance(data, int):
        node = TreeNode(data)
    else :
        raise ValueError("Invalid Input format")
    return node

def find_min(node):
    while node.left is not None:
        node = node.left
    return node.key

def find_max(node):
    while node.right is not None:
        node = node.right
    return node.key

def main():
    data = ((1,2,3),7,((None,9,None),10,11))
    node = makeTree(data)
    print(checkbst(node))
    print(find_min(node))
    print(find_max(node))

if __name__ == "__main__":
    main()
