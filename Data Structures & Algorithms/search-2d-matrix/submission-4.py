class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import numpy as np
        rows = len(matrix)
        columns = len(matrix[0])

        row_iter = 0
        while row_iter < rows:
            if matrix[row_iter][0] < target:
                row_iter += 1
            elif matrix[row_iter][0] == target:
                return True
            else:
                row_iter -= 1
                break
        
        if row_iter == rows:
            row_iter -= 1

        isol_row = matrix[row_iter]

        left = 0
        right = len(isol_row) - 1

        while left <= right:
            mid = (left + right) // 2
            if isol_row[mid] == target:
                return True
            elif isol_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        