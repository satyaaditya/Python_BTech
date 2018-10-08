__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''
import math
def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    s=""
    if(base==2):
        number=  binary(number,base)
        return str(number)
    if(base==16):
       s= hexad(number,base)
       return s
    if(base==20):
       s= power20(number,base)
       return s
    if(base==8):
        number=octal(number,base)
        return str(number)


def binary(number,base):
    i=0;sum=0
    while(number>0):
        r=number%2
        sum=sum+(r*math.pow(10,i))
        i=i+1
        number=number/2
    return int(sum)


def hexad(number,base):
    i=0;lista=[]
    while(number>0):
        r=number%16
        lista.append(r)
        number=number/16
    lista.reverse()
    s=unpack(lista)
    return s.upper()
def unpack(lista):
    a="" ;i=0;
    while(i<len(lista)):
        if((lista[i]>=0)&(lista[i]<=9)):
            a=a+str()
        elif(lista[i]>9):
            x=lista[i]-10
            a=a+chr(97+x)
        i=i+1
    return a

def octal(number,base):
    i=0;sum=0
    while(number>0):
        r=number%8
        sum=sum+(r*math.pow(10,i))
        i=i+1
        number=number/8
    return int(sum)

def power20(number,base):
    a="";lista=[];m=False
    if(number<0):
         m = True
    number = abs(number)
    while(number>0):
        r=number%20
        lista.append(r)
        number = number / 20
    lista.reverse()
    s = unpack(lista)
    if(m==True):
       s='-'+s
    return s.upper()

def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10, 1)
        raise ValueError
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert(10, 40)
        raise ValueError
        assert False, "Invalid base >36 did not raise error"

    except ValueError as ve:
        print ve

    try:
        convert("100", 10)
        raise TypeError
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(None, 10)
        raise TypeError
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(100, "10")
        raise TypeError
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print te

