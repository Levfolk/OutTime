#数值的整数次方
class Solution:
    def mypow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x, n = 1/x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res