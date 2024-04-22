# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        visited = set()
        queue = []
        queue.append(('0000', 0))
        while queue:
            e = queue.pop(0)
            cur = e[0]
            moves = e[1]

            if cur == target:
                return moves
                
            for i in range(4):
                numVal1 = str(int(cur[i]) + 1)
                if numVal1 == "10":
                    numVal1 = "0"
                numVal2 = str(int(cur[i]) - 1)
                if numVal2 == "-1":
                    numVal2 = "9"
                cp1 = cur[:i] + numVal1 + cur[i + 1:]
                cp2 = cur[:i] + numVal2 + cur[i + 1:]
                if cp1 not in visited and cp1 not in deadends:
                    visited.add(cp1)
                    queue.append((cp1, moves + 1))
                if cp2 not in visited and cp2 not in deadends:
                    visited.add(cp2)
                    queue.append((cp2, moves + 1))
        return -1 
