n = int(input())
line = 1

while n > line :
    n -= line
    line += 1
    
if line % 2 == 1 :
    bottom = n
    top = line - n + 1
else :
    top = n
    bottom = line - n + 1
print(top,'/',bottom,sep = '')