class node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else :
            self._insert(value, self.root)

    def _insert(self, value, curNode):
        if value < curNode.value :
            if curNode.left is None :
                curNode.left = node(value)
                curNode.left.parent = curNode
            else :
                self._insert(value, curNode.left)
        elif value > curNode.value :
            if curNode.right is None:
                curNode.right = node(value)
                curNode.right.parent = curNode
            else :
                self._insert(value, curNode.right)
        else :
            print("Value already exists")

    def illustrate(self) :
        if self.root == None :
            print("Tree Doesnt Exist")
        else :
            self._illustrate(self.root)

    def _illustrate(self, curNode, level = 0):
        if curNode == None :
            print("\t" * level + " ")
            return
        self._illustrate(curNode.right, level + 1)
        print("\t" * level + str(curNode.value) + f" h:{curNode.height}")
        self._illustrate(curNode.left, level + 1)

    def height(self):
        if self.root == None:
            return 0
        else :
            return self._height(self.root)

    def _height(self, curNode):
        if curNode == None :
            return -1
        left_height = self._height(curNode.left)
        right_height = self._height(curNode.right)
        return 1 + max(left_height, right_height)

    def search(self, value):
        if self.root == None :
            return False
        else :
            return self._search(self.root, value)

    def _search(self, curNode, value):
        if curNode == None :
            return False
        elif value == curNode.value:
            return True
        if value < curNode.value :
            return self._search(curNode.left, value)
        elif value > curNode.value :
            return self._search(curNode.right, value)

    def inOrderTraversal(self):
        if self.root == None :
            print(" ")
        else :
            self._inOrderTraversal(self.root)

    def _inOrderTraversal(self, curNode):
        if curNode == None :
            return
        self._inOrderTraversal(curNode.left)
        print(f"{curNode.value}", end = " ")
        self._inOrderTraversal(curNode.right)

    def delete(self, value):
        if self.root == None :
            print("No element to delete!")
        else :
            self.root = self._delete(self.root, value)

    def _delete(self, curNode, value):
        if value < curNode.value :
            curNode.left = self._delete(curNode.left, value)
        elif value > curNode.value :
            curNode.right = self._delete(curNode.right, value)
        else :
            if curNode.left == None and curNode.right == None :
                return None
            elif curNode.left and curNode.right == None :
                print("hi")
                return curNode.left
            elif curNode.right and curNode.left == None:
                return curNode.right
            else :
                successor = curNode.right
                while(successor.left != None) : 
                    successor = successor.left
                successor.left = curNode.left
                successor.left.parent = successor
                return curNode.right
        return curNode


def main():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(8)
    tree.insert(10)
    tree.insert(9)
    tree.insert(7)
    tree.illustrate()
    print(f"Height: {tree.height()}")
    print(f"Is value present: {tree.search(1)}")
    print("Inorder Traversal: ", end="")
    tree.inOrderTraversal()
    tree.delete(5)
    tree.illustrate()
    tree.delete(8)
    print("------------------------------------------------------------------")
    tree.illustrate()
    tree.delete(1)
    print("------------------------------------------------------------------")
    tree.illustrate()

if __name__ == "__main__":
    main()
