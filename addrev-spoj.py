n = int(raw_input())
while n:
    a,b = raw_input().split()
    a=a[::-1]
    b=b[::-1]
    a=str(int(a)+int(b))
    a=a[::-1]
    print int(a)
    n-=1