n,case = map(int,input().split())
list = [num for num in range(1,n+1)]
for i in range(case) :
    a,b = map(int,input().split())
    li = list[a-1:b]
    li.reverse()
    for j in range(len(li)) :
        list[a+j-1] = li[j]

print(' '.join(map(str,list)))