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

    def order_up(self):
        return self._order_up(self.root)

    def _order_up(self, node):  # lnr
        if node is None:
            return []
        return self._order_up(node.left) + [node] + self._order_up(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for el in sys.stdin.read().split():
        if el == "0":
            break
        bst.insert(int(el))
    result = [node.data for node in bst.order_up() if (node.left is None) != (node.right is None)]
    print("\n".join(map(str, result)))
