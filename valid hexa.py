import unit6utils

def valid_hexa(file,n):
    hexa_values=[]
    with open(file, 'rt') as f:
        for line in f:
            if set((line.rstrip()).lower()).issubset(set('abcdef123456789')):
                hexa_values.append(line.rstrip())
    hexa_values.sort(key=lambda hexa_number: -int(hexa_number,16))
    return hexa_values[:n]

def test():
    file1 = unit6utils.get_input_file("hexa_file.txt")
    valid_hexa(file1,None)
test()