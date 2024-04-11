# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        for i in range(len(num)):
            cur = int(num[i])
            while stack and int(stack[-1])> cur and k > 0:
                stack.pop(-1)
                k -= 1
            stack.append(num[i])
        stack = stack[:-k] if k > 0 else stack
        ans = "".join(stack).lstrip("0")
        if ans == "":
            return "0"
        return ans
