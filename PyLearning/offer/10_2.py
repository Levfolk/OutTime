#青蛙跳台阶问题
class Solutin:
    def numWays(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

res = Solutin()
print(res.numWays(7))