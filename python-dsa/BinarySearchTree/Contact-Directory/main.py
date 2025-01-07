#from typing import Union

class contact: #contact defination
    def __init__(self, name, number):
        self.name = name 
        self.number = number 

class TreeNode: #BST node defination
    def __init__(self, value = None):
        if value is not None :
            self.key = value.number
        else :
            self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def insert(self, data):
        if self.value is None:
            node = self
            node.key = data.number
            node.value = data
            return node
        node = self
        while(True):
            if data.number > node.key :
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(data)
                    node.right.parent = node
                    break
            elif data.number < node.key :
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(data)
                    node.left.parent = node
                    break
        return node

    def balance(self):
        pass

    def listfy(self):
        arr1 = self.left.listfy() if self.left else []
        arr1.append(self.value)
        arr2 = self.right.listfy() if self.right else []
        return arr1 + arr2

    def parse(self):
        self.left.parse() if self.left else None
        print(self.value.name if self.value else None, end = " ")
        self.right.parse() if self.right else None

def balance():
    pass

def main():
    Tree = TreeNode()
    user0 = contact("z", 7)
    user1 = contact("a", 99)
    user2 = contact("b", 2)
    user3 = contact("c", 1)
    Tree.insert(user0)
    Tree.insert(user1)
    Tree.insert(user2)
    Tree.insert(user3)
    Tree.parse()
    users = Tree.listfy()
    print(users)

if __name__ == "__main__":
    main()
