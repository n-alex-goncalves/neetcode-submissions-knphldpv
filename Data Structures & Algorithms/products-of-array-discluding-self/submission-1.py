class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        total = 1
        for num in nums:
            left.append(total)
            total *= num

        right = []
        total = 1
        for num in nums[::-1]:
            right.append(total)
            total *= num
        right = right[::-1]

        return [x * y for x, y in zip(left, right)]
