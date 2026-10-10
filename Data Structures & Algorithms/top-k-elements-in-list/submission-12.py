import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [x for x, y in heapq.nlargest(k, count.items(), key=lambda x:x[1])]