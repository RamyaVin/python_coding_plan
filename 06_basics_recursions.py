# =============================================================================
# 37	Majority element	https://leetcode.com/problems/majority-element/
### using counter ##O(n)
        frequency_dict = Counter(nums)
        return max(frequency_dict, key = frequency_dict.get)
######leetcode best########### O(NlogN)
def majority(nums):
	nums.sort()
	n = len(nums)
	return nums[n//2]
##################O(N)######
#better code than below 
class Solution:
    def majority(nums):
        count = {}
        max_count = 0
        majority_element = None
        
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                
            if count[num] > max_count:
                max_count = count[num]
                majority_element = num
        
        return majority_element
	    
############### O(N)**2
class Solution:
    def majority(nums):
        return max(set(nums), key = nums.count)
# Driver Code
nums = [10,0, 1,2,1,1,10,10,10,1,1,1,3,7,8]
Solution.majority(nums)

# =============================================================================
# =============================================================================
# 38	Kadane's algo(super imp)	https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(arr,N):
        max_so_far = arr[0]
        max_end = arr[0]
        for num in arr[1:]:
            max_end=max(num,max_end+num)
            max_so_far=max(max_so_far,max_end)
        return max_so_far
# Driver Code
arr = [10,0, 1,2,1,1,-10,-10,10,1,1,1,3,7,8]
Solution.maxSubArraySum(arr,4)
# =============================================================================
# =============================================================================
# 39	Count inversions	https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
"""
The time complexity of the code is O(n log n), where n is the length of the input array arr. This is because the code uses the merge sort algorithm, which has a time complexity of O(n log n) for sorting the array and counting the inversions.
The space complexity of the code is O(n), where n is the length of the input array. This is because the code uses additional space to store the merged subarrays during the merge process. In the worst case, when each element is a separate subarray, the space required is proportional to the length of the array
"""
class Solution:
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount( arr, n):
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

###########same 
class Solution:
    def merge_sort(self, arr, n):
        if n <= 1:
            return arr, 0

        mid = n // 2
        left, inv_left = self.merge_sort(arr[:mid], mid)
        right, inv_right = self.merge_sort(arr[mid:], n - mid)

        merged, inv_merge = self.merge(left, right)

        return merged, inv_left + inv_right + inv_merge

    def merge(self, left, right):
        merged = []
        inversions = 0
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    def inversionCount(self, arr, n):
        _, inversions = self.merge_sort(arr, n)
        return inversions

# Driver Code
A = [4, 3, 2, 1]
num_of_inversions = getNumOfInversions(A)
print("Number of inversions:", num_of_inversions)

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
#####90ms 
class Solution:
    class Solution(object):
    def merge(self, intervals):
        stack = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
      
        stack.append(intervals[0])
        for i in range(1, n):
            x, y = intervals[i]
            stX, stY = stack[-1]
    
            if x <= stY:
                stack[-1][1] = max(stY, y)
            else:
                stack.append([x, y])
    
        ans = []
        while stack:
            ans.append(stack.pop())
    
        return ans[::-1]

#Solution.mergeIntervals([[1,3],[8,10],[15,18],[3,6]])

Solution.mergeIntervals([[1,3],[8,10],[15,18],[3,6]])
##############3merge intervals using stack  - 108 ms
class Solution:
    def mergeIntervals(intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

# Driver Code
intervals = [[1, 3], [8, 10], [15, 18], [3, 6]]
merged_intervals = Solution.mergeIntervals(intervals)
print("Merged intervals:", merged_intervals)
"""
Time complexity:
Original code: The time complexity of the original code is O(n log n), where n is the number of intervals. This is because the code uses the sorted() function to sort the intervals based on their start times, which has a time complexity of O(n log n). The subsequent loop to merge the intervals has a linear time complexity of O(n).
Optimized code: The time complexity of the optimized code is O(n log n), where n is the number of intervals. This is because the code also uses the sorted() function to sort the intervals based on their start times, resulting in a time complexity of O(n log n). The subsequent loop to merge the intervals has a linear time complexity of O(n).
Space complexity:
Original code: The space complexity of the original code is O(n), where n is the number of intervals. This is because the code creates a new list merged to store the merged intervals, which can potentially contain all the intervals from the input list.
Optimized code: The space complexity of the optimized code is O(n), where n is the number of intervals. This is because the code creates a new list merged to store the merged intervals, which will contain at most the same number of intervals as the input list.
"""
# =============================================================================
# =============================================================================
# 41	Maximum product subarray	https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1
"""dynamic programming approach: Instead of calculating the product of all possible subarrays, you can use a dynamic programming approach to keep track of the maximum product at each index."""
#O(N)
class Solution:
    def maxProduct(arr, n):
        if n == 0:
            return 0
        
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        for i in range(1, n):
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
            
            result = max(result, max_product)
        
        return result

# Driver Code
arr = [6, -3, -10, 0, 2]
n = len(arr)
max_product = Solution.maxProduct(arr, n)
print("Maximum product:", max_product)

############### O(N^2)
class Solution:
    def maxProduct(arr, n):
        lis=[]
        if n==1:
            return arr[0]
        for i in range(n):
            k=1
            for j in range(i,n):
                k=k*arr[j]
                lis.append(k)
                if arr[j]==0:
                  break
        return max(lis) 
                
Solution.maxProduct([6, -3, -10, 0, 2],5)
# =============================================================================
# =============================================================================
# 42	Next permutation	https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums):
        for i in range(len(nums)-1, 0, -1):
           # find the index of the last peak
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                # get the index before the last peak
                j = i - 1
                # swap the pre-last peak index with the value just large than it
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                       nums[k], nums[j] = nums[j], nums[k]
                       return nums
        return nums.reverse()
##############33leetcode best solution ##############
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]: i -= 1
        if i >= 0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[:] = nums[:i+1] + nums[i+1:][::-1]
# =============================================================================
# =============================================================================
# 43	Seive of eranthoses(Popular algo for prime numbers)	https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1
"""Use a boolean array instead of an integer array: Instead of using an integer array l to store whether each number is prime or not, you can use a boolean array. This optimization reduces the memory usage and simplifies the code.
Time complexity:

The initialization of the is_prime list takes O(N) time.
The loop to set multiples of 2 as non-prime takes O(N/2) = O(N) time.
The outer loop of the Sieve of Eratosthenes runs up to sqrt(N) and the inner loop runs N/i times for each prime number i. So, the total time complexity for the Sieve of Eratosthenes part is O(sqrt(N) + N/3 + N/5 + ...), which is approximately O(N log log N).
The loop to collect prime numbers takes O(N) time.
Therefore, the overall time complexity of the code is O(N log log N).
Space complexity:
The is_prime list requires O(N) space.
The primes list requires O(N) space in the worst case when all numbers are prime.
Therefore, the overall space complexity of the code is O(N).
"""
class Solution:
    def sieveOfEratosthenes(N):
        def generate_primes():
            is_prime = [True] * (N + 1)  # Initialize boolean array
            # Set multiples of 2 as non-prime
            for i in range(4, N + 1, 2):
                is_prime[i] = False
            # Sieve of Eratosthenes
            for i in range(3, int(N**0.5) + 1, 2):
                if is_prime[i]:
                    for j in range(i*i, N + 1, i):
                        is_prime[j] = False   
            primes = []
            # Collect prime numbers
            for k in range(2, N + 1):
                if is_prime[k]:
                    primes.append(k)
            return primes
        return generate_primes()

# Driver Code
primes = Solution.sieveOfEratosthenes(10)
print("Prime numbers:", primes)
#########################################
class Solution:
    def sieveOfEratosthenes(N):
        def prime(k):
            l=[1 for i in range(N+1)] #setting everything as true
            for i in range(2,int(N**0.5)+1):
                if l[i]==1:
                    for j in range(i*i,N+1,i):
                        l[j]=0 #square of i is false
            return l
        m=[]
        primes=prime(N)
        for k in range(2,N+1):
            if primes[k]==1: #check if true then append that number
                m.append(k)
        return m
Solution.sieveOfEratosthenes(10)
# =============================================================================
# =============================================================================
