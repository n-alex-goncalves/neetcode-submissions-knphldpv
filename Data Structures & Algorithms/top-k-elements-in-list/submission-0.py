class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = collections.Counter(nums)
        freq_list = sorted(list(freq_dict.items()), key = lambda x : x[1], reverse=True)
        return [x for x, y in freq_list[:k]]
        