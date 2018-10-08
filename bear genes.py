from collections import Counter
def get_replace_length(str):
    str=str.lower();length = 0
    k = len(str) / 4
    for i in ('g','c','a','t'):
        if (i in str) == False:
            length+=k
    str=Counter(str)
    for i in str:
        if str[i]<k:
            length+=(k-str[i])
    return length


def check_bear_gene(str,n):
    str=Counter(str)
    for i in str:
        if str[i]<=n:
            pass
        else:
            return 0
    return 1

def bear_gene(str):
    len_to_replace= get_replace_length(str)
    n=len(str)/4
    i=len_to_replace
    while i < len(str):
        j=0
        k=j+i
        while k< len(str):
            if check_bear_gene(str[:j]+str[k:],n):
                print i
                k=len(str)
                i=len(str)
            k+=1;j+=1
        i+=1
bear_gene("agtcgtcc")