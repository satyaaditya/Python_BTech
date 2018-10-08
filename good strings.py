def good_strings(p,a,b,l,r):
        from collections import defaultdict
        index1= defaultdict(list)
        for i in range(int(l)-1,int(r)):
            if p[i]==a:
                index1[0].append(i)
            elif p[i]==b:
                index1[1].append(i)
        from itertools import product
        combinations=list(product(index1[0],index1[1]))
        combinations= [i for i in combinations if i[0]<i[1]]
        print len(combinations)
if __name__=="__main__":
    p = raw_input("string")
    q = int(raw_input("queries"))
    for i in range(q):
        a, b, l, r = raw_input().split()
        good_strings(p,a,b,l,r)

