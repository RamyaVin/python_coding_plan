# =============================================================================
# 37	Majority element	https://leetcode.com/problems/majority-element/

class Solution:
    def majority(nums):
        return max(set(nums), key = nums.count)
# Driver Code
nums = [10,0, 1,2,1,1,10,10,10,1,1,1,3,7,8]
Solution.majority(nums)
### using counter

        frequency_dict = Counter(nums)
        return max(frequency_dict, key = frequency_dict.get)
# =============================================================================
# =============================================================================
# 38	Kadane's algo(super imp)	https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(arr,N):
         max_so_far=float()
         max_end=0
         for num in arr:
            max_end=max(num,max_end+num)
            max_so_far=max(max_so_far,max_end)
         return max_so_far

# Driver Code
arr = [10,0, 1,2,1,1,-10,-10,10,1,1,1,3,7,8]

Solution.maxSubArraySum(arr,4)
# =============================================================================
# =============================================================================
# 39	Count inversions	https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount( arr, n):
        # Your Code Here
        def merge(arr, low, mid, high):
            left = arr[low:mid + 1]
            right = arr[mid + 1:high + 1]
            
            i = 0
            j = 0
            k = low
            cnt = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                    k += 1
                    
                else:
                    arr[k] = right[j]
                    cnt += len(left) - i
                    j += 1
                    k += 1
                    
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
            return cnt

        def merge_sort(arr, low, high):
            cnt = 0
            if low < high:
                mid = (low + high) // 2
                
                cnt += merge_sort(arr, low, mid)
                cnt += merge_sort(arr, mid + 1, high)
                
                cnt += merge(arr, low, mid, high)
                
            return cnt
                
        ans = merge_sort(arr, 0, len(arr) - 1)
        return ans
        

 

arr = [2, 4, 1, 3, 5]

Solution.inversionCount(arr,5)
###

from heapq import heappush, heappop
from bisect import bisect, insort


def getNumOfInversions(A):
	N = len(A)
	if N <= 1:
		return 0

	sortList = []
	result = 0

	# Heapsort, O(N*log(N))
	for i, v in enumerate(A):
		heappush(sortList, (v, i))

	# Create a sorted list of indexes
	x = []
	while sortList:
	
		# O(log(N))
		v, i = heappop(sortList)
		
		# Find the current minimum's index
		# the index y can represent how many minimums on the left
		y = bisect(x, i)
		
		# i can represent how many elements on the left
		# i - y can find how many bigger nums on the left
		result += i - y

		insort(x, i)

	return result
# =============================================================================
# =============================================================================
# 40	Merge intervals	https://leetcode.com/problems/merge-intervals/
# =============================================================================
# =============================================================================
# 41	Maximum product subarray	https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1
# =============================================================================
# =============================================================================
# 42	Next permutation	https://leetcode.com/problems/next-permutation/
# =============================================================================
# =============================================================================
# 43	Seive of eranthoses(Popular algo for prime numbers)	https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1
# =============================================================================
# =============================================================================
