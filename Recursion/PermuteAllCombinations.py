class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        def cal(ip, output):
            if not ip:
                ans.append(output)
            for idx, num in enumerate(ip):
                ip1 = ip.copy()               
                ip1.pop(idx)
                op1 = output.copy()
                op1.append(num)
                cal(ip1, op1)
        cal(nums, [])
        return ans
