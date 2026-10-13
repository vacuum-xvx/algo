stack = []
line = input()
ok = True

for char in line:
    if char in ['(', '{', '[']:
        stack.append(char)
    elif char in [')', '}', ']']:
        if not stack:
            ok = False
            break
        top = stack.pop()
        if (char == ')' and top != '(') or (char == '}' and top != '{') \
            or (char == ']' and top != '['):
            ok = False
            break

print("yes" if not stack and ok else "no")