hour,min = map(int,input().split())
time =int(input())

min += time

if min >= 60 :
    h = min/60
    hour += h
    min %= 60

if hour >= 24 :
    hour -= 24

print(int(hour),min,sep=' ')