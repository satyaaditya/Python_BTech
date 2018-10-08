class Solution(object):
    def myAtoi(self, str1):
        INT_MAX = 2147483647
        INT_MIN =-2147483648
        str1 = raw_input()
        str1 = str1.lstrip(' ')
        str1 = str1.rstrip(' ')
        isneg = False
        if str1[0] == '-':
            isneg = True
        if (str1[0] == '-') or (str1[0]== '+'):
            str1 = str1[1:]

        k = set(map(lambda x : x.isdigit(),str1))
        if len(k) > 1 or not(True in k):
            return 0
        else :
            str1 = int(str1)
            if isneg:
                str1 *= -1
            if str1 > INT_MAX:
                return INT_MAX
            if str1 < INT_MIN:
                return INT_MIN
            return str1