def myfun() :
    list_input = raw_input().split(' ')
    start = int(list_input[0])
    end = int(list_input[1])
    k = int(list_input[2])
    print start,end,k
    count =0
    for i in range(start,end+1):
        if((i- int(str(i)[::-1])))%k==0:
            count+=1
    print count
    '''list_input = raw_input().split(' ')
    i = int(list_input[0])
    j = int(list_input[1])
    k = int(list_input[2])
    count = 0
    for x in range(i, j + 1):
        if (x - int(str(x)[::-1])) % k == 0:
            count += 1
    print(count)'''

myfun()
