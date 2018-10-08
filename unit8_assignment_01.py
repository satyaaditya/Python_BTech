__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

import unit6utils
import string

def number_char_product(word):
    a={ 'a':2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17,'h': 19,'i': 23,'j': 29,'k': 31,
        'l':37,'m': 41,'n': 43,'o': 47,'p': 53,'q': 59,'r': 61,'s':67,'t': 71,'u': 73,'v': 79,'w': 83,'x': 89,'y': 97,'z': 101,}
    l=1
    for i in word:
        l=l*a[i.lower()]
    return l


def anagram_sort(source, destination):
    f=file(source)
    a=f.readlines()
    a = [a[i].strip() for i in range(len(a)) if
         a[i][0] != '#' and a[i][0] != ' ' and a[i] != '\n' and a[i] != ' ']
    a=sorted(a,key=number_char_product)
    b=map(number_char_product,a)
    i=0;j=0
    t=[];c=[]
    try:
     while i<len(b):
        if b[i]==b[j]:
            t.append(a[j])
            j+=1
        else:
            c.append(t)
            t=[]
            i=j
    except IndexError:
        c.append(t)
    c=[sorted(i,key =lambda x:x.lower()) for i in c]
    c=sorted(c,key=lambda x :(len(x),-number_char_product(x[0][0].lower())),reverse=True)
    with open(destination, 'w') as f:
        for s in c:
            for j in s:
                f.write(j + '\n')



if __name__ == "__main__":
    source =unit6utils.get_input_file(sys.argv[1])
    destination=unit6utils.get_temp_file(sys.argv[1][:-4]+'-results.txt')
    anagram_sort(source,destination)
    #sys.exit(main())