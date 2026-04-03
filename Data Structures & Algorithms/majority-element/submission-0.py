class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sorted(freq.items(), key = lambda x:x[1], reverse=True)[0][0]