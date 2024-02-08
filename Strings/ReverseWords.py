class Solution:
    def reverseWords(self, s: str) -> str:
        l = list (reversed(s.split()))
        ans = "" 
        for i in range(0, len(l)):
            if i != len(l) - 1: 
                ans += l[i] + " "
            else:
                ans += l[i]
        return ans
