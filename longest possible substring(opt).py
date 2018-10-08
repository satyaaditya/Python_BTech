def get_mat(m,n):
    a=[[0] for i in range(m)]
    a= [a[i]*n  for i in range(m)]
    return a

def lcs(str1,str2):
    a=get_mat(len(str1)+1,len(str2)+1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                a[i+1][j+1]=1+a[i][j]
            else:
                a[i+1][j+1]= max(a[i][j+1],a[i+1][j])
    j= max(a[0])
    for i in a:
        if max(i)>j:
            j=max(i)
    print (j)



lcs("acbcf","abcdaf")