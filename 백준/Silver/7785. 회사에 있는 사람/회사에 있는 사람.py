n = int(input())
member = {}
for i in range(n) :
    name,inout = map(str,input().split())
    if inout == 'enter' :
        member[name] = 1
    else :
        member[name] = 0
member = member.items()
result = []
for i in member :
    if i[1] == 1 :
        result.append(i[0])
result.sort(reverse=True)        
for i in result :
    print(i)