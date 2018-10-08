def reverse_number(number):
    flag=0
    if number<0:
        flag=1
        number=abs(number)
    number=str(number)
    number=reversed(number)
    number = ''.join(i for i in number)
    number= int(number)
    if flag:
        number = -1 *number
    return number
reverse_number(455)