class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = Counter(nums).items()
        lst = sorted(countNums, key=lambda x:x[1], reverse=True)
        return [x[0] for x in lst[:k]]
