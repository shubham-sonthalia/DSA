# https://leetcode.com/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while True: 
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    count += 1
                if i == k and tickets[i] == 0:
                    return count 
        return 0
