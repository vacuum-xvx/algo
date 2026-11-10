import sys

sys.setrecursionlimit(10000)


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

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node

    def print_tree(self, out):
        self._print_tree(self.root, 0, out)

    def _print_tree(self, node, level, out):
        if node is None:
            return
        self._print_tree(node.left, level + 1, out)
        out.append("." * level + str(node.data))
        self._print_tree(node.right, level + 1, out)


if __name__ == "__main__":
    bst = BinarySearchTree()
    out = []
    for line in sys.stdin:
        command = line.split()
        if not command:
            continue
        if command[0] == "PRINTTREE":
            bst.print_tree(out)
            continue
        key = int(command[1])
        if command[0] == "ADD":
            if bst.search(key):
                out.append("ALREADY")
            else:
                bst.insert(key)
                out.append("DONE")
        elif command[0] == "DELETE":
            if bst.search(key):
                bst.delete(key)
                out.append("DONE")
            else:
                out.append("CANNOT")
        elif command[0] == "SEARCH":
            out.append("YES" if bst.search(key) else "NO")
    print("\n".join(out))
