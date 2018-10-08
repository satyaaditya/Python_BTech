import sys


n,p,q = raw_input().strip().split(' ')
n,p,q = [int(n),int(p),int(q)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
res = [ (i+j)%n for i in a for j in b]
print res;

print max(res);