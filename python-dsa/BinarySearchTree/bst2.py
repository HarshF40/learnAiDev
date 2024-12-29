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

class User:
    def __init__(self, name, uname, email):
        self.name = name
        self.username = uname
        self.email = email

def main():
    jadhesh = User("Jadhesh Verma","jdv99","jd@male.com")
    biraj = User("Biraj Sharma", "bs43", "biraj@kmail.com")
    sonaksh = User("Sonaksh Sinha", "ssop", "sinha@mail.com")
    data = (biraj,jadhesh,sonaksh)
    tree = makeTree(data)
    display(tree)

if __name__ == "__main__":
    main()
