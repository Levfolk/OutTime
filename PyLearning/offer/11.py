class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            m = (left + right) // 2
            if numbers[m] > numbers[right]:
                left = m + 1
            elif numbers[m] < numbers[right]:
                right = m
            else:
                right -= 1
        return numbers[left]
