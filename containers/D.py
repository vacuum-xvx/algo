class Queue:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print('ok')

    def pop(self):
        if not self.items:
            return 'error'
        return self.items.pop(0)

    def front(self):
        if not self.items:
            return 'error'
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        print('ok')


def main():
    queue = Queue()

    while True:
        command = input().split()
        if not command:
            continue

        action = command[0]

        match action:
            case 'push':
                queue.push(int(command[1]))
            case 'pop':
                print(queue.pop())
            case 'front':
                print(queue.front())
            case 'size':
                print(queue.size())
            case 'clear':
                queue.clear()
            case 'exit':
                print('bye')
                break


if __name__ == '__main__':
    main()
