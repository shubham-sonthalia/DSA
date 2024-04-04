# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0 
        for i in s:
            if i == '(':
                count += 1
                max_count = max(max_count, count)
            if i == ')':
                count -= 1
        return max_count

        
