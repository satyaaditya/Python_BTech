__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

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


def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
