# =============================================================================
# Find pair with given sum

def hasArrayTwoCandidates(self,nums, n, k):
	num = {}
	for e in nums:
	    if e in num:
		return 1
	    else:
		num[x - e] = e
	return 0
# =============================================================================
# =============================================================================
# 2 Sum
def twoSum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_indices:
            return [num_indices[diff], i]
        num_indices[num] = i
    return None

# =============================================================================
# =============================================================================
# 3 Sum
def threeSum(nums, target):
    n = len(nums)
    res = []
    nums.sort()

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = n-1

        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]

            if threeSum == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif threeSum < target:
                l += 1
            else:
                r -= 1

    return res             
Solution.threeSum([1,2,1,5],4)
# =============================================================================
# =============================================================================
# 4 Sum
def fourSum(nums, target):
    def helper(nums, target, start, res, temp, num_need):
        if num_need != 2:
            for i in range(start, len(nums) - num_need + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates to avoid duplicate combinations.
                temp.append(nums[i])  # Add the current number to the combination.
                helper(nums, target - nums[i], i + 1, res, temp, num_need - 1)  # Recursively find the next number(s).
                temp.pop()  # Remove the last number to backtrack.
            return

        # If we need exactly 2 numbers, perform a two-pointer approach.
        l, r = start, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                temp.append(nums[l])  # Add the left number to the combination.
                temp.append(nums[r])  # Add the right number to the combination.
                res.add(tuple(temp))  # Store the valid quadruplet in the result set.
                temp.pop()  # Remove the right number to backtrack.
                temp.pop()  # Remove the left number to backtrack.
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1  # Skip duplicates on the left.

    nums.sort()  # Sort the input list in ascending order.
    res = set()  # Use a set to store unique quadruplets.
    temp = []  # Temporary list to store combinations.
    helper(nums, target, 0, res, temp, 4)  # Call the helper function to find quadruplets.
    return [list(quadruplet) for quadruplet in res]  # Convert the set of tuples to a list of lists.
       ############# leetcode best answer ####
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if (len(nums) < 4):
            return []
        
        nums.sort()
        min_sum = nums[0]+nums[1]+nums[2]+nums[3]
        max_sum = nums[-1]+nums[-2]+nums[-3]+nums[-4]

        if target < min_sum or target > max_sum:
            return []
        
        res = []
        num_map = {}
        num_list = []
        sum_map = {}
        for n in nums:
            if n not in num_map:
                num_map[n] = 1
                num_list.append(n)
            else:
                num_map[n] += 1
        
        for i in range(len(num_list)):
            for j in range(i, len(num_list)):
                n = num_list[i]
                m = num_list[j]
                if n != m or num_map[n] >= 2:
                    s = m + n
                    if s not in sum_map:
                        sum_map[s] = []
                    sum_map[s].append((n, m))
        
        for k in sum_map.keys():
            d = target - k

            if d in sum_map and k < d:
                for x, y in sum_map[k]:
                    for m, l in sum_map[d]:
                        if x == y and y == m and m < l and num_map[x] >= 3:
                            res.append([x, x, x, l])
                        elif x < y and y == m and m == l and num_map[l] >= 3:
                            res.append([x, l, l, l])
                        elif x < y and y == m and m < l and num_map[y] >= 2:
                            res.append([x, y, y, l])
                        elif y < m:
                            res.append([x, y, m, l])

        if target % 4 == 0:
            n = target // 4 
            if n in num_map and num_map[n] >= 4:
                res.append([n, n, n, n])

        return sorted(list(res))
# =============================================================================
# =============================================================================
# Find triplets with zero sum
def find_triplets_sum_zero(arr):
    triplets = []
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        x = arr[i]
        while l < r:
            if x + arr[l] + arr[r] == 0:
                triplets.append([x, arr[l], arr[r]])
                l += 1
                r -= 1
            elif x + arr[l] + arr[r] < 0:
                l += 1
            else:
                r -= 1
    return triplets

# Driver code
arr = [0, -1, 5, -3, 2]
triplets = find_triplets_sum_zero(arr)
if len(triplets) > 0:
    for triplet in triplets:
        print(*triplet)
else:
    print("No Triplet Found")

# =============================================================================
# =============================================================================
# Find count of triplets
class Solution:
    def countTriplet(arr, n):
        # code here
        count=0
        s=set(arr)
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if (arr[i]+arr[j]) in s:
                    count+=1
        return count
count =Solution.countTriplet([1, 5, 3, 2],4)   
print("Count of triplets:", count)

# =============================================================================
# =============================================================================
# Union of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
#brute force union of 2 arrays is creating a set and adding array elements to that set
# Python program for the union of two arrays using Set
def getUnion(a, n, b, m):
	# Use set comprehension to get the union set directly
	s = set(a)|set(b)
	return len(s)
	
# Driver Code
if __name__ == '__main__':
	a = [1, 2, 5, 6, 2, 3, 5, 7, 3]
	b = [2, 4, 5, 6, 8, 9, 4, 6, 5, 4]
	getUnion(a, 9, b, 10)
#### hashing
class Solution:
    def printUnion(a, n, b, m):
    	mp = {}
    	 # Inserting array elements in mp
        for i, num in enumerate(a):
            mp[num] = i
    
        for i, num in enumerate(b):
            mp[num] = i
	return(len(mp)) 
    """
    	print("The union set of both arrays is : ")
    	for key in mp.keys():
    		print(key, end=" ")"""
# Driver Code
a = [1, 2, 5, 6, 2, 3, 5]
b = [2, 4, 5, 6, 8, 9, 4, 6, 5]
Solution.printUnion(a, 7, b, 9)
# =============================================================================
# =============================================================================
# Intersection of two arrays
 def ArrayIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        comon=set(a)&set(b)
        return len(comon)

intersection_length = ArrayIntersection([1,2,3],[1,2],3,2)
print(intersection_length)
########
 def ArrayIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
         return len(set(a)&set(b))
intersection_length = ArrayIntersection([1,2,3],[1,2],3,2)
print(intersection_length)
# =============================================================================
# =============================================================================
# Remove duplicates from array(Quite diff from above, try to solve on own, this actually shows that not always you will have pointers at start and end)
class Solution:    
    def remove_duplicate(self, A, N):
	A.append(0)
        if N == 1:
            return N
        i = 0
        j = 1
        while A[j] != 0:
            if A[i]!=A[j]:
                i+=1
                j+=1
            if A[i]==A[j]:
                A.pop(j)
        A.remove(0)
        return len(A)

################
from bisect import bisect_right

def binary_search(nums, low, high, val):
    index = bisect_right(nums, val, low, high)
    return index if index != -1 else len(nums)
	
# =============================================================================
# =============================================================================
# kth element of 2 sorted arrays
class Solution:
    def kElement(a,b,k):
        c=a+b 
        c.sort()
        print(c)
        print(c[k-1])
# Driver Code
a = [1, 2, 5, 6, 2, 3, 5]
b = [1, 2, 5, 6, 2, 3, 5]
k=3
Solution.kElement(a,b,k)
###### above and below same complexity 
"""
riginal code: The time complexity of the original code is O((m + n) log (m + n)), where m and n are the lengths of lists a and b, respectively. This is because the code concatenates the two lists and then performs a sorting operation, which has a time complexity of O((m + n) log (m + n)).

Optimized code: The time complexity of the optimized code is O((m + n) + k log (m + n)), where m and n are the lengths of lists a and b, respectively. This is because the code concatenates the two lists and then uses the nsmallest() function from the heapq module, which has a time complexity of O((m + n) + k log (m + n)).
"""
#heapq module and the nsmallest() function, the code efficiently finds the kth smallest element from the combined list c. The kth smallest element is then returned as the result.

import heapq
class Solution:
    @staticmethod
    def kElement(a, b, k):
        c = a + b
        kth_smallest = heapq.nsmallest(k, c)[-1]
        return kth_smallest
# =============================================================================
# =============================================================================
# Length of longest subarray with sum k
from collections import defaultdict 
class Solution:
    def lenOfLongSubarr (self, arr, nums, k) : 
        #Complete the function
        currsum = 0
        ans = 0
        prefix = defaultdict(int)
        prefix[0] = 0
        
        for i in range(n):
            currsum += arr[i]
            diff = currsum - k
            if diff in prefix:
                size = prefix[diff]
                ans = max(ans,i+1-size)
            if currsum in prefix:
                continue
            else:
                prefix[currsum] = i + 1
        return ans
# =============================================================================
# =============================================================================
# Trapping rain water
class Solution:
     def trappingWater(self, height,n):
        if not height: return 0
        l, r = 0, len(height)-1 
        leftMax, rightMax = height[l], height[r]
        res =  0 
        
        while l < r:
            if leftMax < rightMax:
               l += 1
               leftMax = max(leftMax, height[l])
               res +=  leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax , height[r])
                res +=  rightMax - height[r]
            
        return res
   
# Driver Code
height = [10,0, 9]

Solution.rainTrap(height)

# =============================================================================
