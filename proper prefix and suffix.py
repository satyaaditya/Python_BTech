def get_index(str):
    a=[i for i in range(1,len(str)) if str[0]==str[i]]
    return a

def check_pre_suf(i,str):
    pre=""
    for j in range(len(str)):
        if  i<len(str) and str[j]==str[i]:
            pre+=str[j]
            i+=1
        else:
            if i==len(str):
                return pre
            return ""
def pre_suf(str):
    prev=""
    indices=get_index(str)
    indices=set(indices)
    for i in indices:
        a=check_pre_suf(i,str)
        if len(a)>len(prev):
            prev=a
    print prev

if __name__=="__main__":
    import timeit
    k=timeit.Timer(lambda: pre_suf("abbbab"))
    k=k.repeat(repeat=1,number=1)
    print min(k)
