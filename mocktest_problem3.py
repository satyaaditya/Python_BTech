__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 This is custom encryption scheme that was in popular use to send secret messages in olden days. In this
 scheme successive letters are written in different lines by hand and all the characters are merged line by line
 to create the final encrypted text. The number of lines can differ and is an input to this problem.

 Write encode routine for this cipher given a text and the number of lines n.

 E.g "Hello Cat" with line count 2 when written over 2 lines is:
line1:              H   l   o    C   t
line2:                e   l   ' '  a

    So final text is "HloCtel a" (characters of line 1 followed by characters of line2)

Similarly a word "Popular" with line count 3 will be
line1:            P       l
line2:              o   u   a
line3:                p       r

    So final text is Plouapr

Constraints and notes:
1. Write the cipher routines to work for arbitrary n. Raise value error if n <= 0
2. Assume types are correct
3. Note that the encryption is not done word by word but for the whole text at one go. See the "Hello cat" example, the
   space was treated as part of text and it moved.
4. The problem decomposition is already given for you in the form of 2 routines below. encode must make use of
   get_lines and other python builtin types and features to solve the problem
5. Note that this is a programming problem, don't bother to find out mathematical patterns during the test.
'''

#Implement this generator. Assume n >= 1 as the value checking is done in encode.
def get_lines(number):
    """
    This is an infinite generator returns which line the next character should go to (ie)
    it returns next lines numbers infinitely. For n = 3, it will return 1,2,3,2,1,2,3,2,1,...
    in infinite succession.
    """
    index = 0
    if number == 0:
        yield 0
    while True:
        flag=0;result=1;increment=1
        for i in range(index):
            if flag == number - 1:
                increment *= -1
                flag = 0
            result += increment
            flag += 1
        yield result
        index += 1


# write this routing using the above generator and additional data structures.
def encode(text, n):
    if n<=0:
        raise ValueError

    from collections import defaultdict
    b=defaultdict(list)
    x=get_lines(n)
    for i in text:
        line_no=x.next()
        b[line_no].append(i)
    b=[(b[i]) for i in b]
    final_str=""
    for i in range(len(b)):
        for j in b[i]:
            final_str+=j
    return final_str
#write your own tests
def test_get_lines():
    x=get_lines(2)
    for i in range(10):
        print x.next()

# write your own tests.
def test_encode():
   assert  "HloCtel a" ==encode("Hello Cat",2)

test_encode()