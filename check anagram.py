def number_char_product(word):
    a={ 'a':2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17,'h': 19,'i': 23,'j': 29,'k': 31,
        'l':37,'m': 41,'n': 43,'o': 47,'p': 53,'q': 59,'r': 61,'s':67,'t': 71,'u': 73,'v': 79,'w': 83,'x': 89,'y': 97,'z': 101,}
    l=1
    for i in word:
        l=l*a[i.lower()]
    return l
def anagrams(first, second):
    a=[]
    if ((first==None)|(second==None)):
        return False
    product=number_char_product(first)
    for i in second:
       if product==number_char_product(i):
        a.append(i)
    return a
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])