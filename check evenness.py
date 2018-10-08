def iq_test(numbers):
  b=[];x=''
  numbers=numbers.split()
  numbers= map(lambda x:int(x),numbers )
  c= [int(numbers[i]) for i in range(0,len(numbers)) if int((numbers[i]))%2==0]
  if len(c)==1:
      print numbers.index(c[0])+1
      return numbers.index(c[0])+1
  else:
      z=list(set(numbers)-set(c))
      print (numbers.index(z[0])+1)
      return (numbers.index(z[0]))+1

def a():
    assert 2 == iq_test("1 2 3 3")
    assert 3== iq_test("2 4 7 8 10")
    assert 1 ==iq_test("1 2 2")
    assert 5==iq_test('32 10 24 54 5')
    assert 48==iq_test("79 27 77 57 37 45 27 49 65 33 57 21 71 19 75 85 65 61 23 97 85 9 23 1 9 3 99 77 77 21 79 69 15 37 15 7 93 81 13 89 91 31 45 93 15 97 55 80 85 83")
a()
