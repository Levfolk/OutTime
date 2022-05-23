#递归方法转换进制

#方法一
def toStr1(n, base):
    convertString = "0123456789ABCDEFG"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]

#方法二
rStack = Stack()

def toStr2(n, base):
    convertString = "01234567890ABCDEFG"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr2(n // base, base)