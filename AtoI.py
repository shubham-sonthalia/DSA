class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() # removes white spaces 
        if len(s) == 0: 
            return 0
        isNegative = False
        if s[0] == '-':
            isNegative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        n = len(s)
        num = 0
        zero = ord('0')
        nine = ord('9')
        for i in range(n):
            if ord(s[i]) >= zero and ord(s[i]) <= nine:
                num = num*10 + (ord(s[i]) - zero)
            else:
                break
        if isNegative: 
            return max(-1*num, -(2**31))
        num = min((2**31) -1, num)
        return num
        

        
