def reversewords(p):
    p=p.split('.')
    p='.'.join(p[i] for i in range(len(p)-1,-1,-1))
    print p,'\n'

if __name__=="__main__":
    t= int(raw_input("enter no:of test cases"))
    for i in range(t):
        p=raw_input("enter string")
        reversewords(p)
