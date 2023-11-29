import sys
import math

a,b,v = map(int,input().split())

until = v-a
day = (math.ceil(until / (a-b))) + 1
print(int(day))