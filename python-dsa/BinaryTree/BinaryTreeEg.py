from typing import Union

class TreeNode:
    left : Union["None","TreeNode"]
    right : Union["None","TreeNode"]
    def __init__(self,key):
        self.key = key;
        self.left = None
        self.right = None

def makeTree(data):
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = makeTree(data[0])
        node.right = makeTree(data[2])
    elif data is None:
        node = None
    else :
        node = TreeNode(data)
    return node

def display(node, space='\t', level=0):
    if node is None:
        print(space*level+'?')
        return

    if node.left is None and node.right is None:
        print(space*level+str(node.key))
        return

    display(node.right, space, level+1)
    print(space*level+str(node.key))
    display(node.left, space, level+1)

def treeToTuple(structure):
    if structure is not None:
        if structure.right or structure.left :
            return (treeToTuple(structure.left),structure.key,treeToTuple(structure.right))
        else:
            return structure.key
    else :
        return "None"

def treeToTupleV2(structure):
    if structure is not None and (structure.right or structure.left):
        return (treeToTupleV2(structure.left),structure.key,treeToTupleV2(structure.right))
    elif structure is not None and not (structure.right or structure.left):
        return structure.key
    else:
        return 'None'

def inorderTraverse(node):
    if node.left is not None:
        inorderTraverse(node.left)
        print(node.key, end=" ")
        if node.right is not None:
            inorderTraverse(node.right)
    elif node.left is None or node.right is None:
        print(node.key, end=" ")
        if node.right is not None:
            inorderTraverse(node.right)

def inorderTraverseV2(node):
    if node.left is not None:
        inorderTraverse(node.left)
    print(node.key, end=" ")
    if node.right is not None:
        inorderTraverse(node.right)

def preorderTraverse(node):
    if node is None:
        return
    print(node.key, end=" ")
    preorderTraverse(node.left)
    preorderTraverse(node.right)

def postorderTraverse(node):
    if node is None:
        return None
    postorderTraverse(node.left)
    postorderTraverse(node.right)
    print(node.key,end=" ")

def treeHeight(node):
    if node is None:
        return 0;
    else:
        return 1+max(treeHeight(node.left), treeHeight(node.right))

def count(node):
    if node is None:
        return 0
    else:
        return 1 + count(node.left) + count(node.right)

def main():
    data = ((1,3,(4,6,7)),8,(None,10,(13,14,None)))
    node = makeTree(data)
    treeToTupleOutput = treeToTuple(node)
    treeToTupleV2Output = treeToTupleV2(node)
    print(treeToTupleOutput)
    print(treeToTupleV2Output)
    display(node)
    inorderTraverseV2(node)
    print("")
    preorderTraverse(node)
    print("")
    postorderTraverse(node)
    print("")
    print("")
    print(f"Height: {treeHeight(node)}")
    print(f"Nodes: {count(node)}")

if __name__ == "__main__":
    main()
