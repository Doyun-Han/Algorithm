import sys
n = int(sys.stdin.readline())
result = 0
if n < 4 :
    print(1)
else :
    for i in range(2,n) :
        if (i*i) <= n :
            result += 1
        else :
            break
    print(result+1)