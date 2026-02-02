import sys

def push_f(x):
    stack.insert(0,x)

def push_b(x):
    stack.append(x)

def pop_f():
    if len(stack) == 0:
        return -1
    return stack.pop(0)
    
def pop_b():
    if len(stack) == 0:
        return -1
    return stack.pop(-1)

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def front():
    if len(stack) == 0:
        return -1
    else :
        return stack[0]
        
def back():
    if len(stack) == 0:
        return -1
    else :
        return stack[-1]

stack = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    
    if cmd[0] == 'push_front':
        push_f(cmd[1])
        
    elif cmd[0] == 'push_back':
        push_b(cmd[1])

    elif cmd[0] == 'pop_front':
        print(pop_f())

    elif cmd[0] == 'pop_back':
        print(pop_b())
        
    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'empty':
        print(empty())

    elif cmd[0] == 'front':
        print(front())

    elif cmd[0] == 'back':
        print(back())