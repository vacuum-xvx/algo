import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        curr_node = self.root
        while True:
            if key < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = Node(key)
                    break
                curr_node = curr_node.left
            elif key > curr_node.data:
                if curr_node.right is None:
                    curr_node.right = Node(key)
                    break
                curr_node = curr_node.right
            else:
                break

    def second_max(self):
        parent = None
        current = self.root
        while current.right is not None:  # идём в упор вправо
            parent = current
            current = current.right
        if current.left is None:  # левого нет - ответ родитель (тк и правого нет)
            return parent.data
        current = current.left  # иначе - максимум левого
        while current.right is not None:
            current = current.right
        return current.data


if __name__ == "__main__":
    bst = BinarySearchTree()
    for el in sys.stdin.read().split():
        if el == "0":
            break
        bst.insert(int(el))
    print(bst.second_max())
