def four_power(number):
   number=bin(number)
   number=number[2:]
   if number.count('0')%2==0:
       if number.count('1')==1:
           return 1
       else:
           return 0
   else:
       return 0
def check_if_power_4():
    assert 1 == four_power(1024)
    assert 0 == four_power(401)
    assert 1 == four_power(256)
check_if_power_4()
