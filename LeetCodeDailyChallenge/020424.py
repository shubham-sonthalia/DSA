# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for i in range(len(s)):
            if s[i] in hmap:
                if t[i] != hmap[s[i]]:
                    return False
            else:
                hmap[s[i]] = t[i]
        hmap = {}
        for i in range(len(t)):
            if t[i] in hmap:
                if s[i] != hmap[t[i]]:
                    return False
            else:
                hmap[t[i]] = s[i]
        return True
