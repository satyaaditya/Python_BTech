symbols = {'I' : 1,'X' : 10,'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000,'V' : 5}
roman = raw_input()
decimal = 0
length = len(roman)
for i in xrange(length):
    if i - 1 >=0 and i + 1 <= length-1:
        if (symbols[roman[i-1]] > symbols[roman[i]]) and (symbols[roman[i+1]] > symbols[roman[i]]) :
            decimal -= symbols[roman[i]]
        else:
            decimal += symbols[roman[i]]
    else:
        if i == 0 :
            if i+1<=length-1 and (symbols[roman[i]] < symbols[roman[i+1]]):
                decimal -= symbols[roman[i]]
            else :
                decimal += symbols[roman[i]]
        else:
            decimal += symbols[roman[i]]
print decimal