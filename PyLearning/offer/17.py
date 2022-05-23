class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                res.append(''.join(num))  # 拼接 num 并添加至 res 尾部
                return
            for i in range(10):  # 遍历 0 - 9
                num[x] = str(i)  # 固定第 x 位为 i
                dfs(x + 1)  # 开启固定第 x + 1 位

        def dfs_2(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0':
                    res.append(int(s))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                num[x] = str(i)
                dfs_2(x + 1)
            self.nine -= 1

        num = ['0'] * n  # 起始数字定义为 n 个 0 组成的字符列表
        res = []  # 数字字符串列表
        self.nine = 0
        self.start = n - 1
        dfs_2(0)  # 开启全排列递归
        return res  # 拼接所有数字字符串，使用逗号隔开，并返回



res = Solution()
print(res.printNumbers(3))