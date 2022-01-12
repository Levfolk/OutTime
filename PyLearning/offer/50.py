# 自己的思路：对字符串进行遍历，然后对字符进行计数，找到首个计数为1的字符
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = 0
        for i in s:
            dic[i] += 1
        for key, value in dic.items():
            if value == 1:
                return key
        return ' '


# 题解：使用T/F记录字符出现状态，第一次时记为T，再次出现记为F
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]:
                return c
        return ' '


# 题解改进，使用有序哈希表，由于哈希表是去重的，第二次for循环针对字典遍历次数会少一些
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}  # python 3.6后默认字典为有序的，若是之前版本需使用 dic = collections.OrderedDict() 创建字典
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v:
                return k
        return ' '
