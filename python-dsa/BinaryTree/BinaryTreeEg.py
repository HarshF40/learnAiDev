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

def main():
    data = ((1,3,None), 2, ((None,3,4), 5, (6,7,8)))
    node = makeTree(data)
    treeToTupleOutput = treeToTuple(node)
    treeToTupleV2Output = treeToTupleV2(node)
    print(treeToTupleOutput)
    print(treeToTupleV2Output)

if __name__ == "__main__":
    main()
