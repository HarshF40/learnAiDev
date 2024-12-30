from typing import Union


class BSTnode:
    left: Union["None","BSTnode"]
    right: Union["None","BSTnode"]
    parent: Union["None","BSTnode"]
    def __init__(self, key, value=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def insertd(node, data):
    main = node
    while(True):
        if node.left is not None and data.key < node.key :
            node = node.left
        elif node.right is not None and data.key > node.key :
            node = node.right
        else:
            break
    if data.key > node.key :
        node.right = data
        data.parent = node
    else:
        node.left = data
        data.parent = node
    return main

def illustrate(node, space='\t', level=0):
    if node is None:
        print(space*level+'?')
        return
    if node.left is None and node.right is None:
        print(space*level+str(node.key))
        return
    illustrate(node.right, space, level+1)
    print(space*level+str(node.key))
    illustrate(node.left, space, level+1)

def makeTree(data):
    if data is None:
        return None
    if isinstance(data, tuple) and len(data) == 3:
        node = BSTnode(data[1].username, data[1])
        node.left = makeTree(data[0])
        if node.left:
            node.left.parent = node
        node.right = makeTree(data[2])
        if node.right:
            node.right.parent = node
    elif isinstance(data, User):
        node = BSTnode(data.username, data)
    else:
        raise ValueError
    return node

def display(node):
    if node is None:
        return
    display(node.left)
    print(node.key)
    display(node.right)

def display_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.key))
        if node.left or node.right:  # If there are child nodes
            display_tree(node.left, level + 1, "L--- ")
            display_tree(node.right, level + 1, "R--- ")

class User:
    def __init__(self, name, uname, email):
        self.name = name
        self.username = uname
        self.email = email

def main():
    jadhesh = User("Jadhesh Verma","jdv99","jd@male.com")
    biraj = User("Biraj Sharma", "bs43", "biraj@kmail.com")
    sonaksh = User("Sonaksh Sinha", "ssop", "sinha@mail.com")
    harsh = User("Harsh Gaonker", "harsh", "gaonkarharsh3247@gmail.com")
    data = (biraj,jadhesh,sonaksh)
    tree = makeTree(data)
    #display(tree)
    illustrate(tree)
    print("----------------------------------------------------------------------------------")
    tree = insertd(tree,BSTnode(harsh.username, harsh))
    #display(tree2)
    illustrate(tree)

if __name__ == "__main__":
    main()
