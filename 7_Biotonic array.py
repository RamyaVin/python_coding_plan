# =============================================================================
# 
# What is a 2D Array? How to access element?	
# =============================================================================
# =============================================================================

# Search in a matrix	https://leetcode.com/problems/search-a-2d-matrix/
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target > matrix[i][n - 1]:
                continue
            if target < matrix[i][0]:
                return False
            # for j in range(n):
            #     if target == matrix[i][j]:
            #         return True
            start = 0
            end = n - 1
            mid = -1
            while start <= end:
                mid = start + (end - start) // 2
                if matrix[i][mid] > target:
                    end = mid - 1
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    start = mid + 1
        return False
# =============================================================================
# =============================================================================
# Rotate by 90 degree	https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1
# =============================================================================
# =============================================================================
# Maximum num of 1's row	https://www.geeksforgeeks.org/problems/row-with-minimum-number-of-1s5430/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# Left rotate matrix k times	https://practice.geeksforgeeks.org/problems/left-rotate-matrix-k-times2351/1
# =============================================================================
# =============================================================================
# Print matrix in diagonal pattern	https://www.geeksforgeeks.org/problems/print-matrix-in-diagonal-pattern/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# Set matrix zeros	https://leetcode.com/problems/set-matrix-zeroes/
# =============================================================================
