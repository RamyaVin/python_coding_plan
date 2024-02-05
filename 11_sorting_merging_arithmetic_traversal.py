# =============================================================================
# Sorting, Merging & Related		
# =============================================================================
# =============================================================================
# 68	Find the peak element	https://www.geeksforgeeks.org/problems/peak-element/1?page=1&category=Arrays&difficulty=Medium&status=solved&sortBy=submissions
def findPeak(arr, n):
	l = 0
	r = n-1	
	while(l <= r):
		# finding mid by binary right shifting.
		mid = (l + r) >> 1
		# first case if mid is the answer
		if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
			break
		# move the right pointer
		if(mid > 0 and arr[mid - 1] > arr[mid]):
			r = mid - 1
		# move the left pointer
		else:
			l = mid + 1
	return mid
# Driver Code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print(f"Index of a peak point is {findPeak(arr, n)}")

# =============================================================================
# =============================================================================
# 69	Search element in biotonic array	https://www.interviewbit.com/problems/search-in-bitonic-array/
# Python code to search key in bitonic array

# Function for binary search in ascending part 
def ascendingBinarySearch(arr, low, high, key):	
	while low <= high:
		mid = low + (high - low) // 2
		if arr[mid] == key:
			return mid		
		if arr[mid] > key:
			high = mid - 1
		else:
			low = mid + 1		
	return -1
# Function for binary search in descending part of array
def descendingBinarySearch(arr, low, high, key):	
	while low <= high:
		mid = low + (high - low) // 2
		if arr[mid] == key:
			return mid		
		if arr[mid] < key:
			high = mid - 1
		else:
			low = mid + 1			
	return -1

# Find bitonic point
def findBitonicPoint(arr, n, l, r):
    mid = (r + l) // 2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return mid
    elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        return findBitonicPoint(arr, n, mid, r)
    else:
        return findBitonicPoint(arr, n, l, mid)

# Usage:
bitonicPoint = findBitonicPoint(arr, n, 0, n-1)

# Function to search key in bitonic array
def searchBitonic(arr, n, key, index):
	if key > arr[index]:
		return -1
	elif key == arr[index]:
		return index
	else:
		temp = ascendingBinarySearch(arr, 0, index-1, key)
		if temp != -1:
			return temp
		# search in right of k
		return descendingBinarySearch(arr, index+1, n-1, key)
	
# Driver code
def main():
	arr = [-8, 1, 2, 3, 4, 5, -2, -3]
	key = 1
	n = len(arr)
	l = 0
	r = n - 1
	# Function call
	index = findBitonicPoint(arr, n, l, r)	
	x = searchBitonic(arr, n, key, index)	
	if x == -1:
		print("Element Not Found")
	else:
		print("Element Found at index", x)		
main()

# =============================================================================
# =============================================================================
# Arithmetic(Reversal & traversal - Once you learnt these, you can solve probs in this pattern)		
# =============================================================================
# =============================================================================
# 70	Find row with maximum number of 1's	https://www.geeksforgeeks.org/problems/binary-matrix-having-maximum-number-of-1s--170647/1?page=2&category=Binary%20Search&sortBy=submissions
#User function Template for python3
   def findMaxRow(self, mat, N):
    max_sum = 0
    max_row = 0
    for i in range(N):
        row_sum = sum(mat[i])
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = i
    return max_row, max_sum
# =============================================================================
# =============================================================================
# 71	Search in row wise column wise sorted matrix	https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
"""
However, there are a few issues with the code:
The variable n is used as both the loop variable and the parameter for the number of rows. This can lead to confusion and incorrect results. It is recommended to use a different variable name for the loop variable to avoid conflicts.
The code uses nested loops to iterate over each element of the matrix and check if it matches the target value x. This approach has a time complexity of O(n * m), where n is the number of rows and m is the number of columns. For large matrices, this can be inefficient.
The code returns 1 if the target value is found in the matrix and 0 otherwise. It is better to return a boolean True or False to indicate the presence or absence of the target value. both  have a space complexity of O(1)
""" 
######better ##########time complexity of O(n + m) compared
def search(self, matrix, n, m, x):
    row = 0
    col = m - 1

    while row < n and col >= 0:
        if matrix[row][col] == x:
            return True
        elif matrix[row][col] > x:
            col -= 1
        else:
            row += 1

    return False
	############
def search(self,matrix, n, m, x): 	
        for n in matrix:
                if x in n:
                    return 1
        return 0
### to the initial code's time complexity of O(n * m).
class Solution:
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
        self.width = len(matrix[0])
        self.matrix = matrix
        self.x = x
        for row in matrix:
            if self.bisearch(row, x):
                return 1
        return 0
    def bisearch(self, row, x):
        left = 0
        right = self.width-1
        while left <= right:
            midle = (left+right)//2
            if row[midle] ==x:
                return True
            if row[midle] >x:
                right = midle-1
            else:
                left = midle + 1
        return False
\# =============================================================================
# =============================================================================
# 72	Search in sorted matrix II	https://leetcode.com/problems/search-a-2d-matrix-ii/
def searchMatrix(self, matrix, target):       
	n = len(matrix) ## better runtime than using row and col code alone 
	m = len(matrix[0])
	row = 0
	col = m - 1
	
	while row < n and col >= 0:
	    if matrix[row][col] == target:
		return True
	    elif matrix[row][col] < target:
		row += 1
	    else:
		col -= 1
	return False
# =============================================================================
# =============================================================================
# 73	Find peak in sorted matrix	https://leetcode.com/problems/find-a-peak-element-ii/
class Solution(object):
    def getMaxElement(self, matrix, mid):
        index = -1
        maxi = float('-inf')

        for row in range(len(matrix)):
            elm = matrix[row][mid]

            if elm > maxi:
                maxi = max(maxi, elm)
                index = row

        return index

    def findPeakGrid(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        start = 0
        end = m - 1

        while start <= end:
            mid = start + (end - start) // 2

            # find maximum because we have to check top, bottom, left, right
            # if we use maximum, then our element is definitely greater than top and bottom
            # so we need to check only left and right, i.e., our problem is reduced to finding a peak in 1D

            row = self.getMaxElement(matrix, mid)
            left = -1
            right = -1

            # handling edge cases
            if mid - 1 >= 0:
                left = matrix[row][mid - 1]

            if mid + 1 < m:
                right = matrix[row][mid + 1]

            # we find the peak element
            if matrix[row][mid] > left and matrix[row][mid] > right:
                return [row, mid]

            # our peak is on the left side of mid, so eliminate the right part
            elif matrix[row][mid] > right:
                end = mid - 1

            # our peak is on the right side of mid, so eliminate the left part
            else:
                start = mid + 1

        return [-1, -1]
# =============================================================================
