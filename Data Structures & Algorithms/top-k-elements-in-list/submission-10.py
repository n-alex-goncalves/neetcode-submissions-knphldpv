class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterDictionary = Counter(nums)
        lst = counterDictionary.items()
        return [x for x,y in sorted(lst, key=lambda x:x[1], reverse=True)[:k]]
        