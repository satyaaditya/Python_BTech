def lcs(str1,str2):

    lcs1=[""]
    start_index=0
    for i in range(len(str1)):
        cs1=""
        start=0
        if len(lcs1[0]) >= len(str1[i:]):
            break
        for k in str1[i:]:
            j=start
            if j>=len(str2):
                break
            while j < len(str2):
                if str2[j]==k:
                    cs1+=str2[j]
                    start=j+1
                    break
                j+=1
        if len(lcs1[0])<len(cs1):
            lcs1[0]=cs1
    print lcs1

str1=raw_input()
str2=raw_input()
lcs(str1,str2)