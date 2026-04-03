class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        values = list(freq.items())
        sortedValues = sorted(values, key=lambda x:x[1], reverse=True)
        return [x for x, y in sortedValues][:k]
