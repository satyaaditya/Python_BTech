__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Return the top n most frequently occurring chars and their respective counts in a given string.

e.g "aaaaabbbbccc", 2 should return [('a', 5) ('b', 4)]

in case of a tie, return char which comes later in alphabet ordering first
e.g. "cdbba",2 -> [('b',2), ('d',1)]
     'cdbba',3 -> [('b',2), ('d',1), ('c',1)]

use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars just return the available chars and their counts
4. The function should be case sensitive (ie) A and a are different. So 'aAABBB', 2 should return [('B',3), ('A',2)]
'''
def a(word):
    return (word[1],ord(word[0]))


def top_chars(word, n):
    if (type(word)!=str)|(type(n)!=int):
        raise TypeError
    if n<=0:
        raise ValueError

    c=[]
    from collections import Counter
    b = Counter(word)
    b= [(i,b[i]) for i in b]
    b= sorted(b,key= a,reverse=True)
    if n>len(b):
        n=len(b)
    for i in range(n):
       c.append(b[i])
    return   c




#write your own tests.
def test_top_chars():
    assert [('d',4),('c',3)] ==top_chars("abbcccdddd", 'w')
    assert[('b', 2), ('d', 1), ('c', 1)]==top_chars('cdbba', 3)
    assert [('B', 3), ('a', 2)]==top_chars('aaAABBB', 2)