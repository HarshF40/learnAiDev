from typing import Optional

class node: #contact defination
    def __init__(self, number):
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

    def display(self, space = "\t", level = 0): 
        if self.left is None and self.right is None:
            print(space*level + f"{self.key}")
            return
        self.right.display(space, level+1) if self.right else None
        print(space*level+ f"{self.key}")
        self.left.display(space, level+1) if self.left else None

#def delete(node, key, parent = None):
#    if node is None:
#        print("No Element to delete")
#        return
#    if key > node.key :
#        node.right = delete(node.right, key, node)
#    elif key < node.key :
#        node.left = delete(node.left, key, node)
#
#    if key == node.key:
#        if parent is None:
#            if node.right:
#                node.right.parent = parent
#                next = node.right
#                while next.left is not None:
#                    next = next.left
#                if node.left :
#                    node.left.parent = next
#                    next.left = node.left
#                    node.left = None
#                else :
#                    next.left = None
#                node = node.right
#                return node
#
#            if node.left :
#                node.left.parent = parent
#                node = node.left
#                return node
#                    
#
#        if node.right:
#            if node.key < parent.key if parent else None:
#                parent.left = node.right
#                node.right.parent = parent
#                node.right.left = node.left
#                node = node.right
#                return node
#            if node.key > parent.key if parent else None :
#                parent.right = node.right
#                node.right.parent = parent
#                node.right.left = node.left
#                node = node.right
#                return node
#
#        elif node.left:
#            if node.key < parent.key if parent else None :
#                parent.left = node.left
#                node.left.parent = parent
#                node = node.left
#                return node
#            if node.key > parent.key if parent else None :
#                parent.right = node.left
#                node.left.parent = parent
#                node = node.left
#                return node
#
#        elif node.left is None and  node.right is None:
#            if node.key < parent.key if parent else None :
#                node = None
#                parent.left = node
#                return node
#            elif node.key > parent.key if parent else None :
#                node = None
#                parent.right = node
#                return node
#    return node

def delete(node, key, parent = None):
    if node is None:
        print("No element found to delete")
        return None

    elif key < node.key :
        node.left = delete(node.left, key, node)
    elif key > node.key :
        node.right = delete(node.right, key, parent)
    else :
        if node.left is None and node.right is None :
            return None
        elif node.left is None :
            node.right.parent = parent
            return node.right
        elif node.right is None :
            node.left.parent = parent
            return node.left
        else :
            next = node.right
            while next.left is not None :
                next = next.left
            next.left = node.left
            node.left.parent = next
            return node.right
    return node

def main():
    Tree = TreeNode()
    user0 = node(9)
    user1 = node(6)
    user2 = node(4)
    user3 = node(7)
    user4 = node(3)
    user5 = node(5)
    user6 = node(15)
    user7 = node(11)
    user8 = node(16)
    user9 = node(10)
    user10 = node(13)
    user11 = node(12)
    user12 = node(14)
    Tree.insert(user0)
    Tree.insert(user1)
    Tree.insert(user2)
    Tree.insert(user3)
    Tree.insert(user4)
    Tree.insert(user5)
    Tree.insert(user6)
    Tree.insert(user7)
    Tree.insert(user8)
    #Tree.insert(user9)
    Tree.insert(user10)
    Tree.insert(user11)
    #Tree.insert(user12)
    Tree.display()
    print("----------------------------------------------------------------------------------")
    Tree = delete(Tree, 9)
    Tree.display() if Tree else None

if __name__ == "__main__":
    main()
