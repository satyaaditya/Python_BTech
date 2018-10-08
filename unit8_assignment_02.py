__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

def word_to_worday(word):
    flag=False
    if word[0].isupper():
        flag =True
    if word[0]  in ['a','e','i','o','u']:
         word+='ay'
    else:
        consonant=''
        i=0
        while i<len(word):
            if word[i].lower() in ['a','e','i','o','u']:
                break
            consonant+=word[i]
            i+=1
        word=word[i:]+consonant+'ay'
    if flag:
        return word.capitalize()
    return word
def word_to_piglatin(word):
    piglatin=''
    is_special_char=False
    word= word.split(' ')
    for i in word:
        char=''
        if (i[-1]=='.')|(i[-1]==','):
            char = i[-1]
            i=i[:-1]
            is_special_char=True
        piglatin+=word_to_worday(i)
        if is_special_char:

            piglatin+=char+' '
        else:
            piglatin+=' '
    try:
       while True:
             print piglatin
    except KeyboardInterrupt as ke:
           pass

if __name__ == "__main__":
    import sys
    word_to_piglatin(sys.argv[1])