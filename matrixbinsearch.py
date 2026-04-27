#You are given an m x n 2-D integer array matrix and an integer target.
#Each row in matrix is sorted in non-decreasing order.
#The first integer of every row is greater than the last integer of the previous row.
#Return true if target exists within matrix or false otherwise.
#Can you write a solution that runs in O(log(m * n)) time?
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low = 0
        high = rows - 1
        mid = (low + high) // 2
        while low <= high:
            if target > matrix[mid][-1]:
                low = mid + 1
                mid = (low + high) // 2
            elif target < matrix[mid][0]:
                high = mid - 1
                mid = (low + high) // 2
            else:
                row = mid
                low = 0
                high = cols - 1
                mid = (low + high) // 2
                while low <= high:
                    if target == matrix[row][mid]:
                        return True
                    elif target > matrix[row][mid]:
                        low = mid + 1
                        mid = (low + high) // 2
                    else:
                        high = mid - 1
                        mid = (low + high) // 2
                return False
        return False
