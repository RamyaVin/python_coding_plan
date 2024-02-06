# =============================================================================
# What is a 2D Array? How to access element?	
# =============================================================================
# =============================================================================
# Search in a matrix	https://leetcode.com/problems/search-a-2d-matrix/
#######leetcode best time #################3
   def searchMatrix(self,matrix,target):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==target:
                    return True

        return False  
####################
""" The original code and the optimized code have the same time complexity of O(m * n), where m is the number of rows and n is the number of columns in the matrix. This is because both codes iterate through each row and perform a binary search within each row. The binary search has a time complexity of O(log n), and it is performed for each of the m rows. O(1) since they both use a constant amount of additional space for variables."""
def searchMatrix(matrix, target):
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
##################################
from bisect import bisect_left
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if target > matrix[i][n - 1]:
            continue
        if target < matrix[i][0]:
            return False
        index = bisect_left(matrix[i], target)
        if index < n and matrix[i][index] == target:
            return True
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
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
        return matrix

Solution.rotateby90([[1,3,5],[10,11,16],[23,30,34]], 3)

##########
"""
In terms of time complexity, both the original code and the optimized code have a time complexity of O(n^2), where n is the size of the matrix. This is because both codes iterate through each element of the matrix to reverse the rows and transpose the matrix.
The space complexity of both the original code and the optimized code is O(n^2) since they both create a new matrix to store the rotated matrix.
"""
# =============================================================================
# =============================================================================
# Maximum num of 1's row	https://www.geeksforgeeks.org/problems/row-with-minimum-number-of-1s5430/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
""" Initialize _min with a large value: Instead of initializing _min with float("inf"), you can initialize it with the sum of the first row in the matrix. This avoids unnecessary comparisons and simplifies the code.

Use the enumerate function for tracking the row index: Instead of using a separate variable id to track the row index, you can use the enumerate function to iterate over the matrix and directly access the row index along with the row elements. This improves code readability and eliminates the need for the id variable."""
class Solution:
    #Function to rotate matrix anticlockwise by 90 degrees.
    def minRow(N,M,A):
        _min = sum(A[0]); 
	min_row_id = 0
	    
        for i, row in enumerate(A[1:], start=1):
            curr = sum(row)
            if curr < _min:
                min_row_id = i
                _min = curr
        
        return min_row_id + 1
Solution.minRow(3,3,[[1,1,1],[0,1,0],[0,1,0]])
# =============================================================================
# =============================================================================
# Left rotate matrix k times	https://practice.geeksforgeeks.org/problems/left-rotate-matrix-k-times2351/1
"""
In terms of time complexity, both the original code and the optimized code have a time complexity of O(N * M), where N is the number of rows and M is the number of columns in the matrix. This is because both codes iterate through each element of the matrix to perform the rotation.

The space complexity of both the original code and the optimized code is O(N * M) since they both create a new matrix to store the rotated matrix.
"""
class Solution:
    def rotateMatrix(self, N, M, K, Mat):
        K = K % M
        if K == 0:
            return Mat
        rotated_matrix = [row[K:] + row[:K] for row in Mat]
        return rotated_matrix
# =============================================================================
# =============================================================================
# Print matrix in diagonal pattern	https://www.geeksforgeeks.org/problems/print-matrix-in-diagonal-pattern/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
"""
Use defaultdict for d: Instead of manually checking if a key exists in d and creating an empty list if it doesn't, you can use the defaultdict class from the collections module. This allows you to simply append elements to the list associated with each key without explicitly creating it.
Use list comprehension for constructing res: Instead of using a for loop to iterate over the keys of d and extend res, you can use list comprehension to construct res in a more concise way.
The optimized code uses defaultdict(list) to create d and automatically initializes an empty list for each new key. It then uses list comprehension to construct res by iterating over the keys of d and appending the elements, reversing them for even diagonal indices.
In terms of time complexity, both the original code and the optimized code have a time complexity of O(N^2), where N is the size of the square matrix. This is because both codes iterate through each element of the matrix to construct the diagonal dictionary d.
The space complexity of both the original code and the optimized code is O(N^2) since they both create a new list res to store the rearranged elements.
"""
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
#############################
from collections import defaultdict
class Solution:
    def matrixDiagonally(mat):
        n = len(mat)
        d = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                d[i + j].append(mat[i][j])
        
        res = [elem for key in d for elem in d[key][::-1 if key % 2 == 0 else 1]]
        
        return res
# =============================================================================
# =============================================================================
# Set matrix zeros	https://leetcode.com/problems/set-matrix-zeroes/
#######################leetcode optimised################################3
def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        y = len(matrix)
        x = len(matrix[0])
        for row in range(len(matrix)):
            for num in range(len(matrix[row])):
                if matrix[row][num] == 0:
                    zeros.append((row, num))

        for (r, n) in zeros:
            tr = r
            while tr < y-1:
                matrix[tr+1][n] = 0
                tr +=1
            tr = r
            while tr > 0:
                matrix[tr-1][n] = 0
                tr -= 1
            tn = n
            while tn < x-1:
                matrix[r][tn+1] = 0
                tn += 1
            tn = n
            while tn > 0:
                matrix[r][tn-1] = 0
                tn -= 1
############
""" The time complexity of the code is O(m * n), where m is the number of rows and n is the number of columns in the matrix. This is because the code iterates through each element in the matrix twice.
The space complexity of the code is O(1) because it does not use any additional data structures that grow with the size of the input."""

def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()
    
    y = len(matrix)
    x = len(matrix[0])
    
    # Find the rows and columns containing zeros
    for row in range(y):
        for col in range(x):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)
    
    # Modify the matrix by setting rows and columns to zero
    for row in rows:
        for col in range(x):
            matrix[row][col] = 0
    
    for col in cols:
        for row in range(y):
            matrix[row][col] = 0
Solution.setZeroes([[1,0,14],[10,31,40],[60,15,50]])
# =============================================================================
