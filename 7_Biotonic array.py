# =============================================================================
# 
# What is a 2D Array? How to access element?	
# =============================================================================
# =============================================================================

# Search in a matrix	https://leetcode.com/problems/search-a-2d-matrix/
def searchMatrix(matrix, target):
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
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(matrix, n): 
        # code here
        for row in matrix:
            row.reverse()
            print(row)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
        return matrix

Solution.rotateby90([[1,3,5],[10,11,16],[23,30,34]], 3)
# =============================================================================
# =============================================================================
# Maximum num of 1's row	https://www.geeksforgeeks.org/problems/row-with-minimum-number-of-1s5430/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def minRow(N,M,A):
        _min = float("inf"); id = 1
        for i in range(N):
            curr = sum(A[i])
            if curr < _min:
                id = i + 1; _min = curr
        return id
Solution.minRow(3,3,[[1,1,1],[0,1,0],[0,1,0]])
# =============================================================================
# =============================================================================
# Left rotate matrix k times	https://practice.geeksforgeeks.org/problems/left-rotate-matrix-k-times2351/1
class Solution:
    def rotateMatrix(self,N,M,K,Mat):
        K=K%M
        if K==0:
            return Mat
        rotated_matrix=[]
        for row in Mat:
            rotated_row=row[K:]+row[:K]
            rotated_matrix.append(rotated_row)
        return rotated_matrix
# =============================================================================
# =============================================================================
# Print matrix in diagonal pattern	https://www.geeksforgeeks.org/problems/print-matrix-in-diagonal-pattern/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

class Solution:
    def matrixDiagonally(mat):
        n=len(mat)
        d={}
        for i in range(n):
            for j in range(n):
                if i+j not in d:
                    d[i+j]=[]
                d[i+j].append(mat[i][j])
        res=[]
        for key in d:
            if key%2==0:
                res.extend(d[key][::-1]) #reverse for %2==0
            else:
                res.extend(d[key])
        return res
    
Solution.matrixDiagonally([[1,11,14],[10,31,40],[60,15,50]])

# =============================================================================
# =============================================================================
# Set matrix zeros	https://leetcode.com/problems/set-matrix-zeroes/
# =============================================================================
