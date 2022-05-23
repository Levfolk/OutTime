#十进制数转换被任意进制数
import Stack

#decNumber为原十进制数，base为需要转换为的进制数
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    s = Stack()
    res = ""

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // 2

    while not s.isEmpty():
        res = res + digits[s.pop()]

    return res