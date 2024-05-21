# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def rec(ip, op):
            if not ip:
                ans.add(tuple(op))
                return
            ip1 = ip.copy()
            op1 = op.copy()
            digit = ip1.pop(0)
            op1.append(digit)
            rec(ip1, op)
            rec(ip1, op1)
        rec(nums, [])
        return sorted(list(ans))

                
        
