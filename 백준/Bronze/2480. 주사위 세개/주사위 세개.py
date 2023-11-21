a,b,c = map(int, input().split())
li = [a,b,c]
if a == b:    
    if b==c :
        print(10000+(b)*1000)
    else:
        print(1000+(b)*100)
else:
    if b==c :
        print(1000+(b)*100)
    else:
        if a==c :
            print(1000+(a)*100)
        else:
            li.sort()
            print(li[2]*100)
        