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
	bitonicPoint = 0
	mid = (r + l) // 2
	if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
		return mid
	elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
		bitonicPoint = findBitonicPoint(arr, n, mid, r)
	else:
		bitonicPoint = finsBitonicPoint(arr, n, l, mid)
	return bitonicPoint

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
# =============================================================================
# =============================================================================
# 71	Search in row wise column wise sorted matrix	https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# 72	Search in sorted matrix II	https://leetcode.com/problems/search-a-2d-matrix-ii/
# =============================================================================
# =============================================================================
# 73	Find peak in sorted matrix	https://leetcode.com/problems/find-a-peak-element-ii/
# 
# =============================================================================
