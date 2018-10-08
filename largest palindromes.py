def getpalindrome(substr_len,totalstr_len,str):
    i = substr_len;j=0
    while i<=totalstr_len:
        if i-j==1:  #to eliminate single letter cases
            return ""
        if str[j:i]==str[j:i][::-1]:
            return str[j:i]
        i+=1;j+=1

def checkpalindrome(str):
    b=""
    for i in range(len(str)-1,-1,-1):
        b=getpalindrome(i,len(str),str)
        if b!=None:
            break
    if b=="":
        return "no palindrome exists"
    return b
if __name__=="__main__":
   str=raw_input("enter string")
   print checkpalindrome(str.lower())