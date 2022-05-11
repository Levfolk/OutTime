#求斐波那契数列的第n项,答案对1e9+7取模
class Solutin:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n <= 2:
            return n
        for i in range(n):
            a, b = b, a + b
        return a % 100000007

res = Solutin()
print(res.fib(3))