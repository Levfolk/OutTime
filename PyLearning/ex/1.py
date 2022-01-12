class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i, j in enumerate(nums):
            if target - j in a:
                return [a[target - j], i]
            a[j] = i

"""
nums = [2,7,11,15]
target = 9
a={}
print(nums,"\n")
for i, j in enumerate(nums):
    if target - j in a:
        print("++++",i, j,"++++")
        print(i)
        print(target - j)
        print(a[target - j])
        print(i, a[target - j],"!!!!!!")
    print("\n----",a)
    print("----", i, j, "----")
    a[j] = i
    print("++++",a,"\n")
"""


