import sys
input = sys.stdin.readline
n = int(input())
stack = []
def act(n) :
    if n == 2:
        if len(stack) == 0 :
            return -1
        else :
            num = stack.pop()
            return num
    elif n == 3 :
        return len(stack)
    elif n == 4 :
        if len(stack) == 0 :
            return 1
        else :
            return 0
    else :
        if len(stack) == 0 :
            return -1
        else :
            return stack[-1]

for i in range(n) :
    command = input().rstrip()
    if len(command) > 1 :
        ls = list(map(int,command.split()))
        stack.append(ls[1])
    else :
        print(act(int(command)))