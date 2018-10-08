#Euclid Algorithm
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def return_gcd(numbers):
    numbers=reduce(lambda x,y:get_gcd(x,y),numbers)
    return numbers
def convertFracts(numbers):
    if len(numbers[0])==1:
        denominators=[int(numbers[i][0][1]) for i in range(len(numbers))]
        numerators=[int(numbers[i][0][0]) for i in range(len(numbers))]
    else:
        denominators=[int(i[1]) for i in numbers]
        numerators=[int(i[0]) for i in numbers]
    x= return_gcd(denominators)
    ndform=[[((x*numerators[i])/(denominators[i])),x] for i in range(len(denominators))]
    print ndform
    return ndform

convertFracts([[77033412951888080, 1.4949283383840498e+16], [117787497858827, 1.4949283383840498e+16],
               [2526695441399712, 1.4949283383840498e+16]])
