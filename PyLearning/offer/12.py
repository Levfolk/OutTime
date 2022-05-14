#矩阵中的路径
from collections import Counter
from itertools import chain

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 根据时间消耗最小的题解优化
        if Counter(word) - Counter(chain(*board)):
            return False
        # 即使用Counter计算word和board中的字符数量，如果相减大于0说明board中为包含所有word的字符，立即返回False
        # chain的作用为遍历列表和字符串之类的可迭代对象
        # Counter的原型为Counter(self, iterable)，其中的iterable暂时理解不透测，但可理解为需要一维的数据，所以需要用chain函数处理board


        def dfs(i, j, k):
            if not 0 <= i <= len(board) or not 0 <= j <= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1
            board[i][j] = ' '
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            k += 1
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(Counter(chain(*board)))