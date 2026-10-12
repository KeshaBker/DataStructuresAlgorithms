class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, node):
        new_root = node.left

        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

        new_root.height = 1 + max(
            self.height(new_root.left),
            self.height(new_root.right)
        )

        return new_root

    def rotate_left(self, node):
        new_root = node.right

        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

        new_root.height = 1 + max(
            self.height(new_root.left),
            self.height(new_root.right)
        )

        return new_root

    def insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)

        elif value > node.value:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

        b = self.balance(node)

        if b > 1 and value < node.left.value:
            return self.rotate_right(node)

        if b < -1 and value > node.right.value:
            return self.rotate_left(node)

        if b > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if b < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def add(self, value):
        self.root = self.insert(self.root, value)

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.value]
            + self.inorder(node.right)
        )

    def show(self):
        return self.inorder(self.root)


tree = AVLTree()

tree.add(10)
tree.add(20)
tree.add(30)

print(tree.show())
print(tree.root.value)