def get_opposite_char(str):
    if str is '}':
        return '{'
    if str is ')':
        return '('
    if str is ']':
        return '['

def test_expression(string):
    stack =  [];is_valid = False
    for i in string:
        if((i is '{') or (i is '[') or (i is '(')):
            stack.append(i)
        elif((i is '}') or (i is ']') or (i is ')')):
            j = get_opposite_char(i)
            while len(stack) > 0:
                x = stack.pop()
                if x is j:
                    is_valid = True
                    break
                else: return False
            if not is_valid:
                return False
    if len(stack) is 0:
        return True
    return False

t = int(raw_input())
for i in xrange(t):
    string = raw_input()
    if test_expression(string):
        print "YES"
    else :
        print "NO"