from collections import defaultdict
def getinput():
    b = set()
    while True :
        i = input()
        if i == "":
            break
        b.add(i)
    return b

def getresults1(stats,i):
    if (len(i[2])==4 or len(i[2])==5):
        stats[i[0]][0]+=1
    if (len(i[2])==2 or len(i[2])==3):
        stats[i[0]][1]+=1

    for j in i[2]:
        if j[0]>j[2]:
            stats[i[0]][2]+=1
            stats[i[1]][4]+=1
        elif j[0]<j[2]:
            stats[i[1]][2] += 1
            stats[i[0]][4] += 1
        stats[i[0]][3] += int(j[0])
        stats[i[1]][3] += int(j[2])
        stats[i[0]][5] += int(j[2])
        stats[i[1]][5] += int(j[0])

    return stats

def prio(x):
    return (x[1])

def getresults():
    b=getinput()
    stats=defaultdict(list)
    for i in b:
        i=i.split(':')
        i[2]=i[2].split(',')
        for j in range(2):
            if not i[j] in stats:
                stats[i[j]]
                stats[i[j]]=[0,0,0,0,0,0]
        stats=getresults1(stats,i)
    stats  = [(i,stats[i]) for i in stats]
    stats.sort(key=prio,reverse=True)
    print (stats)
    stats = [' '.join(i) for i in stats ]
    print (stats)