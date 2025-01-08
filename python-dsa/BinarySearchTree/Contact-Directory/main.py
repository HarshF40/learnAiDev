from typing import Optional

class contact: #contact defination
    def __init__(self, name, number):
        self.name = name 
        self.number = number 

class TreeNode: #BST node defination
    left: Optional['TreeNode']
    right: Optional['TreeNode']

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
            self.key = data.number
            self.value = data
            return
        node = self
        while True :
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

    def display(self, space = "\t", level = 0):
        if self.left is None and self.right is None:
            print(space*level + f"{self.key}")
        self.right.display(space, level+1) if self.right else None
        print(space*level+ f"{self.key}")
        self.left.display(space, level+1) if self.left else None

def make_balanced(data, low = 0, high = None, parent = None):
    if high is None:
        high = len(data) - 1
    if low > high:
        return None
    mid = (low + high) // 2
    node = TreeNode(data[mid])
    node.parent = parent
    node.left = make_balanced(data, low, mid-1, node)
    node.right = make_balanced(data, mid+1, high, node)
    return node

def main():
    Tree = TreeNode()
    user0 = contact("z", 0)
    user1 = contact("a", 1)
    user2 = contact("b", 2)
    user3 = contact("c", 3)
    Tree.insert(user0)
    Tree.insert(user1)
    Tree.insert(user2)
    Tree.insert(user3)
    Tree.parse()
    Tree.display()
    users = Tree.listfy()
    Tree = make_balanced(users)
    Tree.display()

if __name__ == "__main__":
    main()
