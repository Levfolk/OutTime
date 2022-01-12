# 自己的思路，遍历列表，发现后一位不等于前一位+1及是缺失的位置
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        if nums[left] != 0:
            return 0
        while left < n - 1:
            if nums[left] == nums[left + 1] - 1:
                left += 1
            else:
                break
        return nums[left] + 1


# 题解，使用二分查找找到缺失位置
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (right + left) // 2
            if nums[m] == m:
                left = m + 1
            if nums[m] != m:
                right = m - 1
        return left
