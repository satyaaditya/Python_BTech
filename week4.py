from itertools import product
from collections import defaultdict
def orangecap(a):

    b=[]
    c=defaultdict(list)
    b=[a[k] for k in a]
    for i in b:
        for j in i:
            c[j].append(i[j])
    a=[(sum(c[i]),i) for i in c]
    a.sort(reverse=True)
    return (a[0][1],a[0][0])

def addpoly(a,b):
    c=defaultdict(list)
    for i in a:
        c[i[1]].append(i[0])
    for j in b:
        c[j[1]].append(j[0])
    c={i:sum(c[i])  for i in c}
    b=[(c[i],i) for i in c if c[i]>0]
    b.sort()
    return b

def multpoly(a,b):
    c=product(a,b)
    c= [(i[0][0]*i[1][0],i[0][1]+i[1][1]) for i in c]
    d=defaultdict(list)
    for i in c:
        d[i[1]].append(i[0])
    c=[(sum(d[i]),i) for i in d if sum(d[i])!=0]
    c.sort(reverse=True)
    return c


assert []==addpoly([(2,1)],[(-2,1)])
assert [(2, 1),(3, 0)]==addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
assert ('Kohli', 120)== orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
assert [(1, 3),(-1, 0)]==multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
