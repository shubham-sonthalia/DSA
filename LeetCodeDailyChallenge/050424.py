# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        if n == 0 or n == 1: 
            return s
        stack = []
        for i in range(n):
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop(-1)
            else:
                stack.append(s[i])
        return ''.join(stack)   
