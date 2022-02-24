#10进制数转换为2进制数
import Stack

def divideBy2(decNumber):
    s = Stack()
    res = ""

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    while not s.isEmpty():
        res = res + str(s.pop())

    return res
