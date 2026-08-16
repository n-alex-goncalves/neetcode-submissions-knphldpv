class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        j = None
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                j = mid
                r = -1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        if j == None:
            return False

        row = matrix[j]
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
            else:
                return True
        
        return False

        