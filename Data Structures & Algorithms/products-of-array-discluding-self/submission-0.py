class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        product = 1
        for i, num in enumerate(nums):
            prefix.append(product)
            product *= num
        
        product = 1
        for i, num in enumerate(nums[::-1]):
            postfix.append(product)
            product *= num
        postfix = postfix[::-1]

        return [x * y for x, y in zip(prefix, postfix)]
        