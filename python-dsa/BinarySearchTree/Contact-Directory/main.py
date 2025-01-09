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
        self.replace(make_balanced(self.listfy()))

    def replace(self,root):
        self.key = root.key
        self.value = root.value
        self.right = root.right
        self.left = root.left
        self.parent = root.parent

    def listfy(self):
        arr1 = self.left.listfy() if self.left else []
        arr1.append(self.value)
        arr2 = self.right.listfy() if self.right else []
        return arr1 + arr2

    def parse(self, count = 0):
        count += self.left.parse() if self.left else 0
        print(self.value.name if self.value else None, end = " ")
        count += self.right.parse() if self.right else 0
        return count + 1

    def display(self, space = "\t", level = 0):
        if self.left is None and self.right is None:
            print(space*level + f"{self.key}")
            return
        self.right.display(space, level+1) if self.right else None
        print(space*level+ f"{self.key}")
        self.left.display(space, level+1) if self.left else None

    def search(self, number):
        if number > self.key :
            val = self.right.search(number) if self.right else print("Not found")
        elif number < self.key :
            val = self.left.search(number) if self.left else print("Not found")
        if number == self.key :
            return self.value
        return val

    def delete(self, key):
        arr = self.listfy()
        low = 0
        high = len(arr) - 1
        mid = None
        found = False
        while low <= high :
            mid = (low + high) // 2
            print(low, mid, high)
            if key == arr[mid].number :
                found = True
                break
            if key > arr[mid].number :
                low = mid + 1
            elif key < arr[mid].number :
                high = mid - 1
        if found and mid is not None:
           del arr[mid]
           self.replace(make_balanced(arr))
        else:
            print("Not found")

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
    user4 = contact("d", 4)
    Tree.insert(user0)
    Tree.insert(user1)
    Tree.insert(user2)
    Tree.insert(user3)
    Tree.insert(user4)
    Tree.display()
    print("---------------------------------------------------------------------------------")
    print(Tree.parse())
    Tree.delete(3)
    print("---------------------------------------------------------------------------------")
    Tree.display()
    print(Tree.parse())

if __name__ == "__main__":
    main()
