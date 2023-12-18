import sys
from collections import deque
d = deque()

input = sys.stdin.readline

case = int(input())
q = deque(enumerate(map(int,input().split())))
ans= []
while q : 
    idx,num = q.popleft()
    ans.append(idx+1)

    if num > 0 :
        q.rotate(-(num - 1))
    else :
        q.rotate(-num)
print(' '.join(map(str,ans)))