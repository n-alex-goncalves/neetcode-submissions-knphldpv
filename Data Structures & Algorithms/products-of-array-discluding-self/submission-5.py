class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        total = 1
        for num in nums:
            l.append(total)
            total *= num

        r = []
        total = 1
        for num in nums[::-1]:
            r.append(total)
            total *= num
        r = r[::-1]

        return [x * y for x, y in zip(l, r)] 