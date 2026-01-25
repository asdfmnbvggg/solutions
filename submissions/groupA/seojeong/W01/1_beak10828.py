import sys

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else :
        return stack[-1]

stack = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    
    if cmd[0] == 'push':
        push(cmd[1])

    elif cmd[0] == 'pop':
        print(pop())

    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'empty':
        print(empty())

    elif cmd[0] == 'top':
        print(top())