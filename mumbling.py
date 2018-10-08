def accum(string):
    b=''
    for i in range(0,len(string)):
        b+=(string[i]*(i+1)).capitalize()
        b+='-'
    b= b.rstrip('-')
    print b
accum("Basic Tests")
