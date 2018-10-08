def matched(string):
    string1=''
    for i in string:
        if (i=='(')|(i==')'):
            string1+=i
    if (string1.count('(')!=string1.count(')'))|(string1.startswith(')')|(string1.endswith('('))):
        return False
    else:
        i=0
        string1=list(string1)
        while i<len(string1):
            if (string1[i]=='(')&(string1[i+1]==')'):
                string1.remove(string1[i])
                string1.remove(string1[i])
                i=0
                continue
            i+=1
        if len(string1)==0:
            return True
        else:
            return False






assert True==matched("zb%78")
assert False==matched("(7)(a")
assert False==matched("a)*(?")
assert True==matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")