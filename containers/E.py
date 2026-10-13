class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, value):
        self.items.insert(0, value)
        print('ok')

    def push_back(self, value):
        self.items.append(value)
        print('ok')

    def pop_front(self):
        if not self.items:
            return 'error'
        return self.items.pop(0)

    def pop_back(self):
        if not self.items:
            return 'error'
        return self.items.pop()

    def front(self):
        if not self.items:
            return 'error'
        return self.items[0]

    def back(self):
        if not self.items:
            return 'error'
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        print('ok')


def main():
    deque = Deque()

    while True:
        command = input().split()
        if not command:
            continue

        action = command[0]

        match action:
            case 'push_front':
                deque.push_front(int(command[1]))
            case 'push_back':
                deque.push_back(int(command[1]))
            case 'pop_front':
                print(deque.pop_front())
            case 'pop_back':
                print(deque.pop_back())
            case 'front':
                print(deque.front())
            case 'back':
                print(deque.back())
            case 'size':
                print(deque.size())
            case 'clear':
                deque.clear()
            case 'exit':
                print('bye')
                break


if __name__ == '__main__':
    main()