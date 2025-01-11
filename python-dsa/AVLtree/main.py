class node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else :
            self._insert(value, self.root)
            self.inspectInsertion(self.root)

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
        curNode.height = self._height(curNode)

    def inspectInsertion(self, curNode, path = []):
        if curNode == None :
            return 
        self.inspectInsertion(curNode.left)
        self.inspectInsertion(curNode.right)
        path.append(curNode)
        lefth = self._height(curNode.left)
        right = self._height(curNode.right)
        if(abs(lefth - right) > 1) :
            print(curNode.value, path[-1].value)
            self.rebalance(path[-1],path[-2],path[-3])

    def rebalance(self, xNode, yNode, zNode):
        if xNode.left == yNode and yNode.right == zNode:
            xNode.left = self.leftRotation(yNode, zNode)
            print(xNode.value, yNode.value, zNode.value)
            node = self.rightRotation(xNode, zNode, yNode)
            xNode.value = node.value
            xNode.parent = node.parent
            xNode.left = node.left
            xNode.right = node.right

    def leftRotation(self, xNode, yNode, zNode = None):
        yNode.left = xNode
        xNode.parent = yNode
        xNode.right = None
        yNode.right = zNode
        return yNode

    def rightRotation(self, xNode, yNode, zNode = None):
        yNode.right = xNode
        xNode.parent = yNode
        xNode.left = None
        yNode.right = zNode
        return yNode

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
            self._heightAfterDelete(self.root)

    def _delete(self, curNode, value):
        if curNode is None:
            print("Number Not found")
            return
        if value < curNode.value :
            curNode.left = self._delete(curNode.left, value)
        elif value > curNode.value :
            curNode.right = self._delete(curNode.right, value)
        else :
            if curNode.left == None and curNode.right == None :
                return None
            elif curNode.left and curNode.right == None :
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

    def _heightAfterDelete(self, curNode):
        if curNode == None:
            return 
        self._heightAfterDelete(curNode.left)
        curNode.height = self._height(curNode)
        self._heightAfterDelete(curNode.right)

def main():

    tree = AVLTree()

    tree.insert(5)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(4)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(6)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(1)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(3)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(8)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(10)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(7)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(9)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.delete(5)
    tree.illustrate()
    print("------------------------------------------------------------------")


    tree.delete(8)
    tree.illustrate()
    print("------------------------------------------------------------------")


    tree.delete(10)
    tree.illustrate()
    print("------------------------------------------------------------------")


    tree.delete(4)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(10)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(11)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(12)
    tree.illustrate()
    print("------------------------------------------------------------------")

    tree.insert(13)
    tree.illustrate()
    print("------------------------------------------------------------------")

if __name__ == "__main__":
    main()
