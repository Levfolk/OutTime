#Code_5.3 有序列表的二分搜索（迭代）
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

#Code_5.4 有序列表的二分搜索（递归）
def binarySearch1(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch1(alist[:midpoint], item)
            else:
                return binarySearch1(alist[midpoint + 1 :], item)