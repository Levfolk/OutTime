#Code_5.5 为字符串构建简单的散列函数
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])     #ord()以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值

    return sum % tablesize

#基于Code_5.5练习，为字符添加权重值
def hash1(astring, tablesize):
    sum = 0
    i = 1 #字符权重
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) * i
        i += 1

    return sum % tablesize