# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j , k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = ''
            if dfs(i, j + 1, k + 1) or dfs(i + 1, j , k + 1) or dfs(i - 1, j , k + 1) or dfs(i, j -1 , k + 1):
                return True
            board[i][j] = temp
            return False    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
