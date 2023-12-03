import sys
cnt = int(sys.stdin.readline())
mylist = [int(sys.stdin.readline()) for _ in range(cnt)]
for i in sorted(mylist) :
    print(i)