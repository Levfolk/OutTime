# 表示数值的字符串
# 思路：确定有限状态自动机，可用于解决【对于给定的输入字符串 S，判断其是否满足条件 P】的一系列问题
class Solution:
    def isNumber(self, s: str) -> bool:
        status = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},
            {'d': 2, '.': 4},
            {'d': 2, '.': 3, 'e': 5, ' ': 8},
            {'d': 3, 'e': 5, ' ': 8},
            {'d': 3},
            {'s': 6, 'd': 7},
            {'d': 7},
            {'d': 7, ' ': 8},
            {' ': 8}
        ]

        p = 0
        for c in s:
            if c == ' ':
                tmp = ' '
            elif c in "0123456789":
                tmp = 'd'
            elif c in "+-":
                tmp = 's'
            elif c in 'eE':
                tmp = 'e'
            elif c == '.':
                tmp = '.'
            else:
                tmp = '?'
            if tmp not in status[p]:
                return False
            p = status[p][tmp]

        return p in (2, 3, 7, 8)
