def isprime(number):
    j=0
    for i in range(1,number+1):
        if number%i==0:
            j+=1
    if j==2:
        return True
    else:
        return False

def sumprimes(list1):
    list1= filter(isprime,list1)
    value=0
    for i in  list1:
        value+=i
    return value

sumprimes([1,2,3,4,5,6,7])