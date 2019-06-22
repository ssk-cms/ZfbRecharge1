x = int(input())
print(",")
y = int(input())
i = int(1)
m = int(2)
n = 0

def fun(x,y):
    if(x!=y):
        x+=1
        fun(x,y)
        n+=1

if -100<=x<=100:
    
    x +=1
    if (x!=y):
        n+=1
        x*=2
    else(x==y):
        n+=1
        break
print(n)