strs = ['ab',"abc","abcd"]
length = len(min(strs))
prefix = ""
for i in xrange(length):
    x = set()
    for j in strs:
        x.add(j[i])
    if len(x) == 1 :
        prefix += x.pop()
    else:
        break
print prefix