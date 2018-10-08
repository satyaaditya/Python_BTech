def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    return a//b

option= {'+':add,'-':sub,'*':mul,'/':div}



operators = ['*','+','-','/',]
tests = int(raw_input())
while tests :
    operator=[];operands=[]
    expr = raw_input()
    i=0
    string = ""
    if expr == '':
        continue
    while expr[i]!= '=':
        if expr[i] in operators :
            operator.append(expr[i])
            operands.append(int(string))
            i+=1
            string = ""
        else :
            if expr[i]>= '0' and expr[i]<='9' :
                string+=expr[i]
                i+=1
            else :
                i+=1
    operands.append(int(string))
    result =operands[0]
    j = operator.__len__()
    k=1
    for i in range(0,j):
        result = option[operator[i]](result,operands[k])
        k+=1

    print result

    tests-=1