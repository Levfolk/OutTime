class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
    x = 100
    str_x = str(x)
    str_x = str_x[::-1]
    print(str_x)
    print(int(str_x))

    y = -123456789
    str_y = str(y)
    print(str_y[:2])
    str_y = str_y[:1:-1]
    print(str_y)
