class Node:
    def __init__(self, value=None):
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
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already exists in the tree.")

        cur_node.height = self._height(cur_node)
        self._rebalance(cur_node)

    def _rebalance(self, cur_node):
        balance = self._balance_factor(cur_node)

        # Left-heavy
        if balance > 1:
            if self._balance_factor(cur_node.left) < 0:
                self._left_rotate(cur_node.left)
            self._right_rotate(cur_node)

        # Right-heavy
        elif balance < -1:
            if self._balance_factor(cur_node.right) > 0:
                self._right_rotate(cur_node.right)
            self._left_rotate(cur_node)

    def _left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        if t2 is not None:
            t2.parent = z

        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y

        z.parent = y

        z.height = self._height(z)
        y.height = self._height(y)

    def _right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        if t3 is not None:
            t3.parent = z

        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y

        z.parent = y

        z.height = self._height(z)
        y.height = self._height(y)

    def _balance_factor(self, cur_node):
        if not cur_node:
            return 0
        return self._height(cur_node.left) - self._height(cur_node.right)

    def _height(self, cur_node):
        if not cur_node:
            return -1
        left_height = self._height(cur_node.left)
        right_height = self._height(cur_node.right)
        return 1 + max(left_height, right_height)

    def illustrate(self):
        if self.root is None:
            print("Tree is empty.")
        else:
            self._illustrate(self.root)

    def _illustrate(self, cur_node, level=0):
        if cur_node is None:
            print("\t" * level + " ")
            return
        self._illustrate(cur_node.right, level + 1)
        print("\t" * level + str(cur_node.value) + f" h:{cur_node.height}")
        self._illustrate(cur_node.left, level + 1)


def main():
    tree = AVLTree()

    values = [5, 4, 6, 1, 3, 8, 10, 7, 9]
    for value in values:
        print(f"Inserting {value}...")
        tree.insert(value)
        tree.illustrate()
        print("-----------------------------------------------------")


if __name__ == "__main__":
    main()

