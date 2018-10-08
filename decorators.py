def log(func):
    def inner(args):
        args=tuple("+91"+i for i in args)
        return func(args)
    return inner
def tes_numbers():
    n=int(raw_input('enter number of phone numbers'))
    num_list=list()
    for i in range(n):
        num_list.append(raw_input('enter phone nummber'))
    num_list=[x if len(x)==10 else  x[-10:] for x in num_list]
    @log
    def decorate(num_list):
        num_list=sorted(num_list)
        '\n'.join(i for i in num_list)
    decorate(num_list)
tes_numbers()

