a,b,c,d,e,f = map(int,input().split())

y = ((c*d)-(f*a))//((b*d)-(a*e))
x = ((c*e)-(b*f))//((a*e)-(b*d))
print(x,y,sep=' ')