mylist = []
maxlen = 0
result = ''
for i in range(5) :
    stringList = list(input())
    if len(stringList) > maxlen :
        maxlen = len(stringList)
    mylist.append(stringList)

for j in range(maxlen) :

    for k in range(5) :
        try :
            string = mylist[k][j]
            result += string
        except :
            continue

print(result)