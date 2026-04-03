class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        lst = matrix[mid]
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            mid = (l + r) // 2
            if lst[mid] < target:
                l = mid + 1
            elif lst[mid] > target:
                r = mid - 1
            else:
                return True
        
        return False

        