n = int(input())
line = 1

while n > line : #분수는 사선 line의 갯수만큼 원소를 가지므로 n번째 라인에서 m번째를 구하기 위해 사용
    n -= line
    line += 1

if line % 2 == 1 :
    bottom = n
    top = line - n + 1
else :
    top = n
    bottom = line - n + 1
print(top,'/',bottom,sep = '')