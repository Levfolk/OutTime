class Solution:
    def maxDepth(self, s: str) -> int:
        ans, cur = 0, 0
        for i in s:
            if i == '(':
                cur += 1
                ans = max(ans, cur)
            if i == ')':
                cur -= 1
        return ans
