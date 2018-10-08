def is_a_prime(num):
    for i in xrange(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def prime_generator():
    prev_prime=2;x=3
    yield 2
    while True:
            if is_a_prime(x) and x!=prev_prime:
                prev_prime=x
                yield x
            x+=2

def fib_series():
    prev=1
    yield 1;pres=1
    while True:
        yield pres
        prev,pres= pres,prev+pres

def get_comm_series(seq1,seq2):
    seq1=iter(seq1)
    seq2=iter(seq2)
    x=seq1.next()
    y=seq2.next()
    while True:
        if x==y:
            yield y
            x=seq1.next()
            y=seq2.next()
        elif x>y:
            y=seq2.next()
        else:
            x=seq1.next()

if __name__=="__main__":
    x=get_comm_series(prime_generator(),fib_series())
    for i in xrange(9):
        print x.next()
#get_comm_series(prime_generator(),fib_series())
