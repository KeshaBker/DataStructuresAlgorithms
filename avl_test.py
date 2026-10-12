from avl import AVLTree


def test_add():
    tree = AVLTree()

    tree.add(10)
    tree.add(20)
    tree.add(30)

    assert tree.show() == [10, 20, 30]


def test_balance():
    tree = AVLTree()

    tree.add(10)
    tree.add(20)
    tree.add(30)

    assert tree.root.value == 20