#二进制中1的个数
class Solution:
    #方法一：n & 1
    def hammingWeight_1(self, n):
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res

    #方法二：n & (n - 1)
    def hammingWeight_2(self, n):
        res = 0
        while n > 0:
            res + n & (n - 1)
            n -= 1
        return res
