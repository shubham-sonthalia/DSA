class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        r = s[::-1]
        c = r[0]
        l = 0
        while c != ' ':
            l += 1
            if l < len(r):
                c = r[l]
            else:
                break
        return l 
