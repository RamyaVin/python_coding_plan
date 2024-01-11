# =============================================================================
# Find pair with given sum
class Solution():
   def arraySum(nums,k):
       sumdict={0:1}
       count=0
       s=0
       for num in nums:
           s+=num
           if s-k in sumdict:
               count+=sumdict[s-k]
           if s in sumdict:
               sumdict[s]+=1
           else:
               sumdict[s]=1
       return count
Solution.arraySum([1,2,3,2],4)
# =============================================================================
# =============================================================================
# 2 Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        preMap = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in preMap:
                return [preMap[diff],i]
            preMap[n]=i
        return

# =============================================================================
# =============================================================================
# 3 Sum
class Solution():
    def threeSum(nums, target):
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                threeSum=nums[i]+nums[l]+nums[r]
                if threeSum==target: 
                    res.append([nums[i],nums[l],nums[r]])
                    return res
                elif threeSum<target:
                    l+=1
                else:
                    r-=1
            return res                  

Solution.threeSum([1,2,1,5],4)
# =============================================================================
# =============================================================================
# 4 Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
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
                    res.append(temp[:])  # Store the valid quadruplet in the result list.
                    temp.pop()  # Remove the right number to backtrack.
                    temp.pop()  # Remove the left number to backtrack.
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # Skip duplicates on the left.

        nums.sort()  # Sort the input list in ascending order.
        res = []  # Result list to store valid quadruplets.
        temp = []  # Temporary list to store combinations.
        helper(nums, target, 0, res, temp, 4)  # Call the helper function to find quadruplets.
        return res  # Return the result list containing unique quadruplets.
       #############
    # Python3 program to find four 
    # elements with the given sum
    
    # Function to find 4 elements that
    # add up to given sum 
    def fourSum(X, arr, Map, N):
        temp = [0 for i in range(N)]
        # Iterate from 0 to length of arr 
        for i in range(N - 1):
            
            # Iterate from i + 1 to length of arr
            for j in range(i + 1, N):
                
                # Store curr_sum = arr[i] + arr[j] 
                curr_sum = arr[i] + arr[j]
    
                # Check if X - curr_sum if present 
                # in map 
                if (X - curr_sum) in Map:
                    
                    # Store pair having map value 
                    # X - curr_sum 
                    p = Map[X - curr_sum]
    
                    if (p[0] != i and p[1] != i and
                        p[0] != j and p[1] != j and
                        temp[p[0]] == 0 and temp[p[1]] == 0 and
                        temp[i] == 0 and temp[j] == 0):
                            
                        # Print the output 
                        lists=[arr[i], arr[j],arr[p[0]],arr[p[1]]]
                        print(lists)
                        print(arr[i], ",", arr[j], ",", 
                            arr[p[0]], ",", arr[p[1]], 
                            sep = "")
                            
                        temp[p[1]] = 1
                        temp[i] = 1
                        temp[j] = 1
                        break
    
    # Function for two Sum 
    def twoSum(nums, N):
        
        Map = {}
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                Map[nums[i] + nums[j]] = []
                Map[nums[i] + nums[j]].append(i)
                Map[nums[i] + nums[j]].append(j)
    
        return Map
    
    # Driver code
    arr = [ 10, 20, 30, 40, 1, 2 ]
    n = len(arr)
    X = 91
    Map = twoSum(arr, n)
    
    # Function call 
    fourSum(X, arr, Map, n)

# =============================================================================
# =============================================================================
# Find triplets with zero sum
class Solution():
        
    def findTriplets(arr, n):
    
    	found = False
    
    	# sort array elements
    	arr.sort()
    
    	for i in range(0, n-1):
    
    		# initialize left and right
    		l = i + 1
    		r = n - 1
    		x = arr[i]
    		while (l < r):
    
    			if (x + arr[l] + arr[r] == 0):
    				# print elements if it's sum is zero
    				print(x, arr[l], arr[r])
    				l += 1
    				r -= 1
    				found = True
    
    			# If sum of three elements is less
    			# than zero then increment in left
    			elif (x + arr[l] + arr[r] < 0):
    				l += 1
    
    			# if sum is greater than zero then
    			# decrement in right side
    			else:
    				r -= 1
    
    	if (found == False):
    		print(" No Triplet Found")
    

# Driven source
arr = [0, -1, 5, -3, 2]
n = len(arr)
Solution.findTriplets(arr, n)                  
# =============================================================================
# =============================================================================
# Find count of triplets
class Solution():
        
        # Python3 program to find four 
    # elements with the given sum
    
    # Function to find 4 elements that
    # add up to given sum 
    def fourSum(X, arr, Map, N):
        temp = [0 for i in range(N)]
        count=0
        # Iterate from 0 to length of arr 
        for i in range(N - 1):
            
            # Iterate from i + 1 to length of arr
            for j in range(i + 1, N):
                
                # Store curr_sum = arr[i] + arr[j] 
                curr_sum = arr[i] + arr[j]
    
                # Check if X - curr_sum if present 
                # in map 
                if (X - curr_sum) in Map:
                    
                    # Store pair having map value 
                    # X - curr_sum 
                    p = Map[X - curr_sum]
    
                    if (p[0] != i and p[1] != i and
                        p[0] != j and p[1] != j and
                        temp[p[0]] == 0 and temp[p[1]] == 0 and
                        temp[i] == 0 and temp[j] == 0):
                            
                        # Print the output 
                        lists=[arr[i], arr[j],arr[p[0]],arr[p[1]]]
                        count+=1 
                        print(arr[i], ",", arr[j], ",", 
                            arr[p[0]], ",", arr[p[1]], 
                            sep = "")
                        print(lists)
                        if j==N-2: print("Count of triplet sets: " , count)
                        
                            
                        temp[p[1]] = 1
                        temp[i] = 1
                        temp[j] = 1
                        break
        
                    
    # Function for two Sum 
    def twoSum(nums, N):
        
        Map = {}
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                Map[nums[i] + nums[j]] = []
                Map[nums[i] + nums[j]].append(i)
                Map[nums[i] + nums[j]].append(j)
    
        return Map
    
    # Driver code
    arr = [ 10, 20, 30, 40, 1, 20, 69, 1,1]
    n = len(arr)
    X = 91
    Map = twoSum(arr, n)
    
    # Function call 
    fourSum(X, arr, Map, n)
#Solution.findTriplets(arr, n)               
# =============================================================================
# =============================================================================
# Union of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
# =============================================================================
# =============================================================================
# Intersection of two arrays
# =============================================================================
# =============================================================================
# Remove duplicates from array(Quite diff from above, try to solve on own, this actually shows that not always you will have pointers at start and end)
# =============================================================================
# =============================================================================
# kth element of 2 sorted arrays
# =============================================================================
# =============================================================================
# Length of longest subarray with sum k
# =============================================================================
# =============================================================================
# Trapping rain water
# =============================================================================
