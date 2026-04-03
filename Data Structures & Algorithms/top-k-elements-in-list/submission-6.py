class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        values = sorted(count.items(), key = lambda x:x[1], reverse=True)
        return [x for x, y in values[:k]]
        