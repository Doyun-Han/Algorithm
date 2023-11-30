import math
m = int(input())
n = int(input())
mylist = []

for i in range(m,n+1) :
    if i == 1 :
        continue
    if i == 2 :
        mylist.append(2)
        continue

    sqrt = math.ceil(math.sqrt(i))
    isTrue = True
    for j in range(2,sqrt+1) :
        if i%j == 0 :
            isTrue = False
            break
    if isTrue == True :
        mylist.append(i)

if len(mylist) == 0 :
    print(-1)
else :
    print(sum(mylist))
    print(min(mylist))