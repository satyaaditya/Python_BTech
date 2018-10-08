def palindromes(str):
    from itertools import permutations
    a=list(permutations(str))
    a= filter(lambda x:x==x[::-1],a)
    print set(a)

palindromes("abc")