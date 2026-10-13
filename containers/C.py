line = input()
stack = []

for char in line:

    if char.isdigit():
        stack.append(int(char))

    elif char in ['+', '-', '*']:
        a = stack.pop()
        b = stack.pop()

        if char == '+':
            stack.append(b + a)
        elif char == '-':
            stack.append(b - a)
        elif char == '*':
            stack.append(b * a)

print(stack.pop())