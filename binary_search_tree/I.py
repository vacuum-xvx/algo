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

    def is_balanced(self):
        return self._check_height(self.root) != -1

    def _check_height(self, node):  # высота поддерева или -1, если дисбаланс
        if node is None:
            return 0
        left_height = self._check_height(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_height(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for el in sys.stdin.read().split():
        if el == "0":
            break
        bst.insert(int(el))
    print("YES" if bst.is_balanced() else "NO")
