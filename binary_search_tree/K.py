import sys


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

    def next_value(self, key):
        answer = -1
        current = self.root
        while current is not None:
            if current.data >= key:
                answer = current.data
                current = current.left # вдруг есть еще меньше
            else:
                current = current.right # мы меньше, идем вправо
        return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    bst = BinarySearchTree()
    n = int(input())
    last = None  # None если перед "+" был НЕ "?"
    out = []
    for _ in range(n):
        op, value = input().split()
        value = int(value)
        if op == "+":
            if last is None:  # начало или после другого "+"
                bst.insert(value)
            else:
                bst.insert((value + last) % 10 ** 9)
            last = None
        else:
            last = bst.next_value(value)
            out.append(str(last))
    print("\n".join(out))
