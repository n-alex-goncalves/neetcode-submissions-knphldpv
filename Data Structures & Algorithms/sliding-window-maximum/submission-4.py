class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        l, r = 0, 0
        condition r = r - l + 1 < k
        condition l = else
        '''
        l, r = 0, 0

        output = []
        maxHeap = [(nums[0], 0)]
        heapq.heapify_max(maxHeap)
 
        while r < len(nums):
            print(l, r)
            if r - l + 1 < k:
                r += 1       
                if r < len(nums):
                    heapq.heappush_max(maxHeap, (nums[r], r))
            else:
                output.append(maxHeap[0][0])
                while maxHeap and maxHeap[0][1] <= l:
                    heapq.heappop_max(maxHeap)
                l += 1
        
        return output