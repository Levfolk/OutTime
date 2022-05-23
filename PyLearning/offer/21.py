#调整数组顺序使奇数位于偶数前
class Solution:
    #快慢指针
    def exchange(self, nums: List[int]) -> List[int]:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] & 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums

    #头尾指针
    def exchange_2(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 1:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums