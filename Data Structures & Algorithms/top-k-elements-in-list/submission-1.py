import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = collections.Counter(nums)
        numFrequency = sorted(list(numFrequency.items()), key = lambda x : x[1], reverse=True)
        return [x[0] for x in numFrequency[:k]]