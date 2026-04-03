class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freqNum = list(freq.items())
        return [x for x, y in sorted(freqNum, key=lambda x:x[1], reverse=True)[:k]]