# =============================================================================
# Must solve other probs(Try to solve these probs on own, brute force atleast you can come up for most of them after solving above)		
# =============================================================================
# 74	Aggressive cows	https://www.geeksforgeeks.org/problems/aggressive-cows/1?page=1&category=Binary%20Search&sortBy=submissions
    def solve(self,n,k,stalls):
        pass
        stalls.sort()
        l , h = 1 , stalls[-1] - stalls[0]
        def cowsAccomodated(m): #m no. of cows
            prev = stalls[0]
            temp = 1
            for i in range(1,len(stalls)):
                if stalls[i] - prev >= m:
                    temp += 1
                    prev = stalls[i]
                if temp == k: return True
            return False
      
        ret = 0
        while l <= h:
            m = (l + h) // 2
            if(cowsAccomodated(m)):
                ret = m
                l = m + 1
            else: h = m - 1
        return ret
# =============================================================================
# =============================================================================
# 75	Allocate minimum pages	https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
#Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if(M>N):
            return -1
        l = max(A)
        h = sum(A)
        while(l<=h):
            m = (l+h)//2
            if(self.stdcnt(A,m)>M):
                l = m+1
            else:
                h = m-1
        return l
    
    def stdcnt(self,A,pages):
        std = 1
        pagecnt = 0
        for i in range(len(A)):
            if(pagecnt+A[i]<=pages):
                pagecnt+=A[i]
            else:
                std+=1
                pagecnt = A[i]
        return std
# =============================================================================
# =============================================================================
# 76	Painter partition	https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1?page=1&category=Binary%20Search&sortBy=submissions
   
    def isPossible(self, arr, n, k, mid):
        painters_required = 1
        current_length = 0
        for i in range(n):
            current_length += arr[i]
            if current_length > mid:
                painters_required += 1
                current_length = arr[i]
        return painters_required <= k
    def minTime(self, arr, n, k):
        low = max(arr)
        high = sum(arr)
        while low < high:
            mid = (low + high) // 2
            if self.isPossible(arr, n, k, mid):
                high = mid
            else:
                low = mid + 1
        return lo
# =============================================================================
# =============================================================================
# 77	Split array largest sum	https://www.geeksforgeeks.org/problems/split-array-largest-sum--141634/1?page=2&category=Binary%20Search&sortBy=submissions
    def splitArray(self, arr, N, k):
        # code here 
        start,runtotal=arr[0],0
        for item in arr:
            start=max(start,item)
            runtotal+=item
        while start<=runtotal:
            mid=(start+runtotal)//2
            if self.is_possible(arr,k,mid):
                runtotal=mid-1
            else:
                start=mid+1
        return runtotal+1
    
    def is_possible(self,arr,k,mid):
        curr_sum=0
        cuts=0
        for item in arr:
            curr_sum+=item
            if curr_sum>mid:
                curr_sum=item
                cuts+=1
        return k>cuts
# =============================================================================
# =============================================================================
# 78	Minimum num of days to make m bouquets	https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        val = m * k #m-boquet, k no. of flowers in boquet , flowers to be adjacent
        if val > n: return -1 # if flowers required is greater than len(arr) boquet not possible
        low = float('inf')
        high = float('-inf')
        for day in bloomDay:
            low = min(day, low)   #min in arr
            high = max(day, high) #max in arr
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(bloomDay, mid, m, k):       high = mid - 1
            else:            low = mid + 1    
        return low
    
    def possible(self, bloomDay, day, m, k): #mid=day
        cnt,num=0,0
        for bd in bloomDay:
            if bd <= day: cnt += 1
            else:
                num += cnt // k     #cnt - no. of flowers , num - no. of boquets
                cnt = 0
        num += cnt // k
        return num >= m
# =============================================================================
# =============================================================================
# 79	Capacity to ship packages within D days	https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1?page=2&category=Binary%20Search&sortBy=submissions
    def loaded(self,arr,mid):
        days=1
        load=0
        N=len(arr)
        for i in range(N):
            if load+arr[i]>mid:
                days+=1
                load=arr[i]
            else:
                load+=arr[i]
        return days
    def leastWeightCapacity(self, arr, N, D):
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high - low) // 2
            if self.loaded(arr, mid) <= D:
                high = mid - 1
            else:
                low = mid + 1
        return low
# =============================================================================
# =============================================================================
# 80	koko eating bananas	https://leetcode.com/problems/koko-eating-bananas/
def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) / 2
            if self.canEatAll(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def canEatAll(self, piles, speed, h):
        time = 0
        for pile in piles:
            time += (pile - 1) / speed + 1
            if time > h:
                return False
        return True
# =============================================================================
# =============================================================================
# 81	kth smallest number in matrix multiplication table	https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
def findKthNumber(self, m, n, k):        
        # Define binary search function to find the kth smallest element
        def binary_search(left, right):
            while left < right:
                mid = (left + right) // 2
                count = 0
                j = n
                for i in range(1, m+1):
                    while j >= 1 and i*j > mid:
                        j -= 1
                    count += j
                if count < k:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # Call binary search function with appropriate left and right bounds
        return binary_search(1, m*n)
# =============================================================================
# =============================================================================
# 82	kth smallest pair distance	https://leetcode.com/problems/find-k-th-smallest-pair-distance/

def smallestDistancePair(nums, k):
    # Return: Is there k or more pairs with distance <= guess? i.e. are
    # there enough?
    def possible(guess_dist):
        i = count = 0
        j = 1
        # Notice that we never decrement j or i.
        while i < len(nums):
            # If the distance calculated from j-i is less than the guess,
            # increase the window on `j` side.
            while (j < len(nums)) and ((nums[j] - nums[i]) <= guess_dist):
                j += 1
            # Count all places between j and i
            count += j - i - 1
            i += 1
        return count >= k

    nums.sort()
    lo = 0
    hi = nums[-1] - nums[0]

    while lo < hi:
        mid = (lo + hi) // 2
        # If `mid` produced `k` or more results we know it's the upper bound.
        if possible(mid):
            # We don't set to `mid - 1` because we found a number of distances
            # bigger than *or equal* to `k`. If this `mid` ends up being
            # actually equal to `k` then it's a correct guess, so let's leave it within
            # the guess space.
            hi = mid
        # If `mid` did not produce enouh results, let's increase  the guess
        # space and try a higher number.
        else:
            lo = mid + 1

    # `lo` ends up being an actual distance in the input, because
    # the binary search mechanism waits until the exact lo/hi combo where
    # 2nd to last `mid` did not produce enough results (k or more), but
    # the last `mid` did.
    return lo
# =============================================================================
# =============================================================================
# 83	Ugly number II	https://leetcode.com/problems/ugly-number-ii/   ## ugly number when multiple of 2 or 3 or 5
class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]
# =============================================================================
# =============================================================================
# 84	Median of 2 sorted arrays	Median of 2 Sorted Arrays of Different Sizes | Practice | GeeksforGeeks
# A Simple Merge based O(n) solution to find
""" 
Assumption in this function: 
Both ar1[] and ar2[] are sorted arrays """
def getMedian(ar1, ar2, n, m):

	i = 0 # Current index of input array ar1[]
	j = 0 # Current index of input array ar2[]
	m1, m2 = -1, -1
	for count in range(((n + m) // 2) + 1):
		if(i != n and j != m):
			if ar1[i] > ar2[j]:
				m1 = ar2[j]
				j += 1
			else:
				m1 = ar1[i]
				i += 1
		elif(i < n):
			m1 = ar1[i]
			i += 1
			# for case when j<m,
		else:
			m1 = ar2[j]
			j += 1
		# return m1 if it's length odd else return (m1+m2)//2
	return m1 if (n + m) % 2 == 1 else (m1 + m2) // 2
# Driver code
ar1 = [900]
ar2 = [5, 8, 10, 20]

n1 = len(ar1)
n2 = len(ar2)
print(getMedian(ar1, ar2, n1, n2))
# =============================================================================
# =============================================================================
# 85	Find smallest divisor given threshold	Find the Smallest Divisor Given a Threshold - LeetCode
# 
# =============================================================================
