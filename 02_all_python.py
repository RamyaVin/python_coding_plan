# =============================================================================
# Find even or odd
class Solution:
    def evenOdd(x):
        if x%2 ==1: return "Odd"
        else: return "Even"
        
print(Solution.evenOdd(4))
# =============================================================================
# =============================================================================
# Find last digit in a number
class Solution:
    def lastDigit(x):
        return abs(x%10)
        
print(Solution.lastDigit(40190))
# =============================================================================
# =============================================================================
# Count digits in a number(Solving above last digit prob wil make this easy for you)
class Solution:
    def countDigits(x):
        count=0
        while x!=0:
            x//=10
            count+=1
        return count

print(Solution.countDigits(4090))
# =============================================================================
# =============================================================================
# Reverse a number(Try thinking how you can use above logic in solving this)
class Solution():
    def reverse( x):
        if x > 2 ** 31 - 1 or x < -(2 ** 31):
            return 0
        
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10
        result = sign * reverse
        return result
    
Solution.reverse(345345601)
# =============================================================================
# =============================================================================
# Find power of a number
#12**21/(10**9+7)
class Solution():
    def powerOfNumber( x):
        if x > 2 ** 31 - 1 or x < -(2 ** 31):
            return 0
        
        reverse = 0
        sign = -1 if x < 0 else 1
        temp=x
        x = abs(x)
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10
        result = sign * reverse
        mod=10**9 + 7
        print(temp,result,mod)
        return print(pow(temp,result,mod))
    
    
Solution.powerOfNumber(12)

# =============================================================================
# =============================================================================
# GCD
class Solution():
    def GCD(a,b):
        rem=1
        if a > b:
            dividend=a
            divisor=b
        else: 
            dividend=b
            divisor=a
        while rem!=0:
            rem=dividend%divisor
            if rem!=0:
                dividend=divisor
                divisor=rem
        return divisor             
            
Solution.GCD(120,40)

# =============================================================================
# =============================================================================
# Print all divisors of a number
class Solution():
    def sum_divs(n):
        i = 1
        s=[]
        while i <= n//2 : 
            if (n % i==0) : 
                s.append(i)
            i+=1
        s.append(n)
        return s
                         
Solution.sum_divs(45)
# =============================================================================
# =============================================================================
# Prime number(Try solving by yourself)
class Solution():
    def prime(n):
        flag=0
        for i in range(2, n//2, 1 ): 
            if (n%i==0): 
                flag=1               
                break
        if flag==1: print("Not Prime")
        else: print("Prime")
        return
    
Solution.prime(139)
# =============================================================================
# =============================================================================
# Armstrong number(Solving power of number, will make this easy for you)
#1^3 + 5^3 + 3^3 equals 153
class Solution():
    def armstrong(n):
        result=0
        digits=len(str(n))
        for i in range(1, n): 
            result=result+(n%10)**(digits)
            n=n//10
        return result
    
Solution.armstrong(123)
# =============================================================================
# =============================================================================
# Check palindrome of number(Use the techniques you learnt so far solving above probs and solve this by yourself)
class Solution():
    def palindrome(n):
        x=str(n)
        if x==x[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome" 
    
Solution.palindrome(100)
# also palindrom of negative number 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        div = 1
        while x >= 10 * div:
            div*=10

        while x:
            if x // div != x % 10:return False 
            x = (x % div) // 10 
            div = div/100

        return True
# =============================================================================
# =============================================================================
# Square root of a number(Try to first figure out algo to solve this)
class Solution():
    def squareRoot(n):
        if n>0: flag=1
        else: flag=-1
        return flag*(abs(n)**(1/2) )
    
Solution.squareRoot(-100)
# =============================================================================
# =============================================================================
# Perfect number
# a positive integer that is equal to the sum of its proper divisors. 6 = 1,2,3 = 1+2+3=6 is perfect number
class Solution():
    def perfectNumber(n):
        total=0
        for i in range(1,n//2+1):
            if n%i==0: 
                total=total+i
                print(i,"i")
                print(total,"total")
            else: 
                i+=1
        print(total)
        if total == n:
            print(n , "is a perfect number")
            return "Perfect number" 
        else: 
            return "Not perfect number"
    
Solution.perfectNumber(61)
# =============================================================================
# =============================================================================
# What is an array? How is it represented?
# =============================================================================
# =============================================================================



Solution.maxMinArray([11,2,3,4,21])

# =============================================================================
# =============================================================================
# Find third largest element in array
class Solution():
    def max3Array(s):
        s=sorted(s)
        print(s[2])
        
Solution.max3Array([11,2,3,4,21])

# =============================================================================
# =============================================================================
# Search an element in array(Understand how to traverse through the array and how to access the elements)
class Solution():
    def Array(s,target):
        n = len(s)
        for i in range(0,n,1):
            if s[i]==target:
                print("Number in array at location", i )
Solution.Array([11,2,3,4,21],3)
# =============================================================================
# =============================================================================
# Find missing number in array
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return ((n * (n+1)) // 2 ) - sum(nums)

# =============================================================================
# =============================================================================
# Find repeating number in array
class Solution():
    def repeatingNumber(nums):
        
        n = len(nums)-2
        return sum(nums)-((n * (n+1)) // 2 ) 
    
Solution.repeatingNumber([0,2,3,4,3,1])
# =============================================================================
# =============================================================================
# Sort an array of 0s , 1s and 2s (You dont need to know any sorting algo, just using basics, once solved, definitely learn the optimal algo)
class Solution():
    def sortArray(nums):
        n=len(nums)
        low,mid,high=0,0,n-1
        while (mid<=high):
            if(nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif (nums[mid]==1):
                mid+=1
            else:
                #nums[mid]=2
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums
    
Solution.sortArray([0,2,1,2,0,1])

# =============================================================================
# =============================================================================
# Check if two arrays are equal or not
class Solution():
    def equalArray(x,y):
        flag=0
        if len(x) == len(y):
            for i in range(0,len(x),1):
                if x[i] != y[i]:flag=1
                break
            return True if flag ==0 else False
        else:
            return False
    
Solution.equalArray([1,2,1,2,0,1],[1,2,1,2,0])
# =============================================================================
# =============================================================================
# Rotate the array by 1
class Solution():
    def rorateArray_1(nums):
        nums.append(nums[0])
        nums.pop(0)
        return nums
    
Solution.rorateArray_1([3,2,1,2,0,1])
# =============================================================================
# =============================================================================
# Rotate the array by k
class Solution(object):
    def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        if k == 0:
            return nums
        while k//len(nums)!=0:
                k=k-len(nums)
        nums.reverse()
        print(nums)
        nums[:k] = reversed(nums[:k])
        print(nums)
        nums[k:] = reversed(nums[k:])
        print(nums)
        return nums
Solution.rotate([3,2,1,2,0,1],2)

# =============================================================================
# =============================================================================
# Array subset of another array
class Solution():
    def arraySubset(a,b):
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in b:
            if i not in d:
                return "No"
            elif i in d and d[i]==0:
                return "No"
            else:
                d[i]-=1
        return "Yes"
        
Solution.arraySubset([5,2,3,1],[1,0,3])
# =============================================================================
# =============================================================================
# Learn what is map and how its represented before moving forward

# =============================================================================
# =============================================================================
# Count frequency of elements in array(Solve efficiently, try applying what you learnt about map)
class Solution():
    def arrayFreq(a):
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return d
                
Solution.arrayFreq([5,2,3,1,1,2])

# =============================================================================
# =============================================================================
# =============================================================================
#find pair with given sum
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		# code here
        temp = set()
        for i in range(n//2+1):
            diff1 = x - arr[i]
            diff2 = x - arr[n-i-1]
            if diff1 in temp or diff2 in temp:
                return True
            temp.add(arr[i])
            temp.add(arr[n-i-1])
        return False
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
    

# Driver code
arr = [0, -1, 5, -3, 2]
n = len(arr)
Solution.findTriplets(arr, n) 

###triples print sum =0 in array 
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
# =============================================================================
# =============================================================================
# Find count of triplets
class Solution:
    def countTriplet(arr, n):
        # code here
        count=0
        s=set(arr)
        '''
        or
        for i in arr:
            s.add(i)
        '''
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if (arr[i]+arr[j]) in s:
                    count+=1

        return count
                    

Solution.countTriplet([1, 5, 3, 2],4)          
# =============================================================================
# =============================================================================
# Union of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
brute force union of 2 arrays is creating a set and adding array elements to that set
# Python program for the union of two arrays using Set
def getUnion(a, n, b, m):

	# Defining set container s
	s = set()

	# Inserting array elements in s
	for i in range(n):
		s.add(a[i])

	for i in range(m):
		s.add(b[i])
	print("Number of elements after union operation: ", len(s), "")
	print("The union set of both arrays is :" + "")

	print(s, end="") # s will contain only distinct
	# elements from array a and b


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
    	for i in range(n):
    		mp[a[i]] = i
    
    	for i in range(m):
    		mp[b[i]] = i
    
    	print("The union set of both arrays is : ")
    	for key in mp.keys():
    
    		print(key, end=" ")
    

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
        return(len(comon))
ArrayIntersection([1,2,3],[1,2],3,2)
#####
class Solution:
    def printIntersection(arr1, arr2, m, n):
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        while(i < m and j < n):
            if(arr1[i] < arr2[j]):
                i += 1
            elif(arr2[j] < arr1[i]):
                j += 1
            else:
                print(arr2[j])
                j += 1
                i += 1
               
# Driver Code
a = [1, 2, 5, 6, 2, 3, 5]
b = [2, 4, 5, 6, 8, 9, 4, 6, 5]

Solution.printIntersection(a, b,7,9)
# =============================================================================
# =============================================================================
# Remove duplicates from array(Quite diff from above, try to solve on own, this actually shows that not always you will have pointers at start and end)
class Solution:
    def printIntersection(a,  n):
        a.sort()
        print(a)
        s=list()
        duplicate=[]
        for i in range (0,n-1,1):
            if a[i]!=a[i+1]:
                s.append(a[i])
            elif a[i]==a[i+1]:
                duplicate.append(a[i])
        return s,duplicate
         
    
# Driver Code
a = [1, 2, 5, 6, 2, 3, 5]

Solution.printIntersection(a, 7)
###########

def binary_search(nums, low, high, val):
	n = len(nums)
	res = -1
	while low <= high:
		mid = low + (high - low) // 2
		if nums[mid] <= val:
			low = mid + 1
		else:
			res = mid
			high = mid - 1
	if res == -1:
		return n
	return res

def remove_duplicates(nums):
	n = len(nums)
	idx = 0 # It stores the indexing of unique elements.

	while idx != n:
		i = binary_search(nums, idx + 1, n - 1, nums[idx]) # It finds the upper bound of the element.

		if i == n: # Means we are not able to find the upper bound of the element.
			return idx + 1
		idx += 1
		nums[idx] = nums[i]
	
	return idx + 1

# Driver code
if __name__ == "__main__":
	arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]

	# remove_duplicates() returns the new size of the array.
	n = remove_duplicates(arr)

	# Print the updated array
	for i in range(n):
		print(arr[i], end=" ")
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
# =============================================================================
# =============================================================================
# Length of longest subarray with sum k
class Solution:
    def lenOfLongSubarr (self, arr, nums, k) : 
        #Complete the function
        currsum = 0
        ans = 0
        prefix = {}
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
    def rainTrap(height):
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
class Solution:
    def mergeIntervals(intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        merged = [intervals[0]]
        for interval in intervals:
            # Normal case not overlaping
                print(merged[-1][1],interval[0], intervals)
                if merged[-1][1] < interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

Solution.mergeIntervals([[1,3],[8,10],[15,18],[3,6]])
# =============================================================================
# =============================================================================
# 41	Maximum product subarray	https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1
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
    def nextPermutation(nums):
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
# =============================================================================
# =============================================================================
# 43	Seive of eranthoses(Popular algo for prime numbers)	https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1
class Solution:
    def sieveOfEratosthenes(N):
        #code here
    
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
class Solution:
    def setZeroes(matrix):

        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        # iterate through matrix to mark the zero row and cols
        for row in range(m): #1st element of row 0
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
        print(matrix)
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):  #1st element of col = 0 then entire col =0
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        print(matrix)
        # update the first row and col if they're zero
        print(first_row_has_zero,"first_row_has_zero")
        if first_row_has_zero: # if True "0"
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
        return matrix
Solution.setZeroes([[1,0,14],[10,31,40],[60,15,50]])
# =============================================================================
# =============================================================================
# 51	Print 1 to N using recursion	https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1
class Solution:    
    def printNos(self,n):
        #Your code here
        if n==0:
            return 1
        else:
            
            self.printNos(n-1)
            print(n,end=" ")
            
Solution.printNos()
# =============================================================================
# =============================================================================
# 52	Factorial of N numbers	https://practice.geeksforgeeks.org/problems/factorial5739/1
class Solution:    
    def factorial(self,n):
        if n==0: return 1
        else: 
            return(n*self.factorial(n-1))
            
# =============================================================================
# =============================================================================
# 53	Fibonacci series using recursion	https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

class Solution:
    def nthFibonacci(self, n : int) -> int:
        a=0
        b=1
        mod=1000000007
        for i in range(1,n):
            c=(a+b)%mod
            a=b
            b=c
            
        return c
### with recursion 
# Python code to implement Fibonacci series

# Function for fibonacci
def fib(n):

	# Stop condition
	if (n == 0):
		return 0

	# Stop condition
	if (n == 1 or n == 2):
		return 1

	# Recursion function
	else:
		return (fib(n - 1) + fib(n - 2))


# Driver Code

# Initialize variable n.
n = 5;
print("Fibonacci series of 5 numbers is :",end=" ")

# for loop to print the fibonacci series.
for i in range(0,n): 
	print(fib(i),end=" ")

# =============================================================================
# =============================================================================
# 54	Power(x,n) Draw the recursion tree for all the probs for sure	https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        
        return pow(N,R,1000000007)
# =============================================================================
# =============================================================================
# 55	Print pattern	https://www.geeksforgeeks.org/problems/print-pattern3549/1?page=1&category=Recursion&difficulty=Easy&sortBy=submissions

def pattern(N):
    # code here
    if N <= 0:
        return [N,]
    
    a = list(range(N, -5, -5))
    return a + a[::-1][1:]
pattern(16)

# =============================================================================
# =============================================================================
# 56	Recursive implementation of atoi	https://practice.geeksforgeeks.org/problems/implement-atoi/1?utm_source=geeksforgeeks&utm_medium=ml_Article_practice_tab&utm_campaign=Article_practice_tab

##
def atoi(string):
      try:
            return int(string)
        except:
            return -1
##
def atoi(string):
        if string[0]=='-':
            if all(c.isdigit() for c in string[1:]):
                return int(string)
        elif all(c.isdigit() for c in string):
            return int(string)
        return -1
        # Code here
        
atoi("-123a")

# =============================================================================
# =============================================================================
# 57	Pascal triangle	https://www.geeksforgeeks.org/problems/pascal-triangle0652/1?page=1&category=Recursion&difficulty=Easy&sortBy=submissions
 def nthRowOfPascalTriangle(n):
        # code here
        if n==1:
            return([1])
        if n==2:
            return([1,1])
        l=[1]
        k=nthRowOfPascalTriangle(n-1)
        for i in range(len(k)-1):
            l.append((k[i]+k[i+1])%(10**9 +7))
        l.append(1)
        return(l)
    
nthRowOfPascalTriangle(10)
# =============================================================================
# =============================================================================
# Basics	Bubble sort(very basic sorting technique)	https://www.geeksforgeeks.org/problems/bubble-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    
        # code here
# =============================================================================
# =============================================================================
# Basic patterns	Completely understand how Node in linkedList is represented and then go ahead with the patterns	


# =============================================================================
# =============================================================================
# 58	Search in a sorted array(Efficiently -> So learn binary search for this)	https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?page=1&category=Binary%20Search&sortBy=submissions
#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        l=0
        h=N-1
        while(l<=h):
            mid=(l+h)//2
            if arr[mid]==K:
                return 1
            elif arr[mid]>K:
                h=mid-1
            elif arr[mid]<K:
                l=mid+1
        return -1
        
# =============================================================================
# =============================================================================
# 59	Find floor and ceil in sorted array	https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
def findFloor(A,N,K):
        #Your code here
        low = 0
        high = N-1
        count = 0 
        while(low <= high):
            mid = (low + high)//2 #sort and merge algo
            if A[mid] > K:
                high = mid-1
            elif A[mid] < K:
                if (mid+1 < N) and A[mid+1] > K:
                    return mid
                low = mid+1
                count = 1
            else:
                return mid
        if count == 0:
            return -1
        return mid # array pos where a[mid] is 
            
K = 6
N = 7
A= [2, 4, 5, 7, 8, 9, 10]
findFloor(A, N, K)

# =============================================================================
# =============================================================================
# 60	Find first and last occurence of element in sorted array	https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1?page=1&category=Binary%20Search&sortBy=submissions
#User function Template for python3


class Solution:
    def f1(self,arr,l,h,x):
        ans=-1
        while(l<=h):
            m=(l+h)//2
            if(arr[m]<=x):
                l=m+1
            else:
                h=m-1
            if(arr[m]==x):
                ans=m
        return ans
    def s1(self,arr,l,h,x):
        ans=-1
        while(l<=h):
            m=(l+h)//2
            if(arr[m]>=x):
                h=m-1
            else:
                l=m+1
            if(arr[m]==x):
                ans=m
        return ans
        
                
    def find(self, arr, n, x):
        f=self.f1(arr,0,n-1,x)
        s=self.s1(arr,0,n-1,x)
        return [s,f]
        
####
import bisect

def find(arr, n, x):
    
    # code here
    first = bisect.bisect_left(arr, x)
    if arr[first] != x:
        return [-1, -1]
    last = bisect.bisect_right(arr, x) - 1
    return [first, max(last, 0)]

            
x = 5
n = 8
arr= [2, 4, 5, 5, 7, 8, 9, 10]
find(arr, n, x)
# =============================================================================
# =============================================================================
# 61	Find missing num from 1 to N	https://leetcode.com/problems/missing-number/

def missingNumber(self, nums):
    n = len(nums)
    return ((n * (n+1)) // 2 ) - sum(nums)
# =============================================================================
# =============================================================================
# 62	Find square root	https://www.geeksforgeeks.org/problems/square-root/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
def p(x):
    return pow(x,0.5

p(4)
# =============================================================================
# =============================================================================
# 63	Search for element in infinite array	https://www.codingninjas.com/studio/problems/search-in-infinite-sorted-0-1-array_696193
def firstOne(get):
    # Write your code here.
    # This function returns the first index of the occurence of 1
    pass
    low = 0
    high = int(1e18) #10**18+1
    while low <= high:
        mid = low + (high - low) // 2
        if get(mid) == 1:high = mid - 1
        else:low = mid + 1
    return low
# =============================================================================
# =============================================================================
# 64	Search element in sorted rotated array(With and without duplicate)	https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
 ### without sort 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
                # If the length of the given array list is 1, then check the first element and return accordingly
        if len(nums)==1:
            if nums[0]!=target:
                return False
            else:
                return True

        left=0
        right=len(nums)-1
        # binary search 
        while(left<=right):

            # shifting to remove duplicate elements
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1

            # step 1 calculate the mid    
            mid=(left+right)//2

            #step 2
            if nums[mid]==target:
                return True

            #step 3
            elif nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1

            # step 4
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        # step 5
        return False
# =============================================================================
# =============================================================================
# 65	Minimum element in sorted rotated array(With and without duplicate)A twist in normal BS is needed, once you learnt this, solve the below by yourself,even try to solve this also by yourself	https://www.geeksforgeeks.org/problems/minimum-number-in-a-sorted-rotated-array-1587115620/1?page=1&category=Binary%20Search&sortBy=submissions
#User function Template for python3
class Solution:
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        #Your code here
        while (low<high):
            mid= low+(high-low)//2
            if (arr[mid]>arr[high]):
                low=mid+1
            else:
                high=mid
        return arr[low]
##
#also 
return min(arr)
##or
sort(arr)
return arr[0]
# =============================================================================
# =============================================================================
# 66	Number of times array is sorted	https://www.geeksforgeeks.org/problems/rotation4723/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
def findKRotation(arr, n):
        # code here
    low= 0
    high = n-1
    while (low<high):
        mid= low+(high-low)//2
        if (arr[mid]>arr[high]):
            low=mid+1
        else:
            high=mid
    return low 

n = 4
arr = [4, 5, 2, 3]
findKRotation(arr, n)
# =============================================================================
# =============================================================================
# 67	Maximum element in sorted rotated array	
# Function to return the maximum element
def findMax(arr, low, high):

	# If there is only one element left
	if (high == low):
		return arr[low]

	# Find mid
	mid = low + (high - low) // 2
	# Check if mid reaches 0 ,it is greater than next element or not
	if(mid==0 and arr[mid]>arr[mid+1]):
		return arr[mid]

	# Check if mid itself is maximum element
	if (mid < high and arr[mid + 1] < arr[mid] and mid>0 and arr[mid]>arr[mid-1]):
		return arr[mid]
	
# Decide whether we need to go to
	# the left half or the right half
	if (arr[low] > arr[mid]):
		return findMax(arr, low, mid - 1)
	else:
		return findMax(arr, mid + 1, high)

# Driver code
arr = [6,5,4,3,2,1]
n = len(arr)
print(findMax(arr, 0, n - 1))
# =============================================================================
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
#User function Template for python3
   def findMaxRow(self, mat, N):
            # Code here
        max=0
        row=0
        for i in range(N):
            if max<sum(mat[i]):
               max=sum(mat[i])
               row=i
        if row==0 and max==0:
            row=0
            max=0
            
            return row,max
        else:
            return row,max
# =============================================================================
# =============================================================================
# 71	Search in row wise column wise sorted matrix	https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
def search(self,matrix, n, m, x): 	
        for n in matrix:
                if x in n:
                    return 1
        return 0
###
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
# 
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

# =============================================================================
# Selection sort	https://www.geeksforgeeks.org/problems/selection-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
    def selectionSort(self, arr,n):
        for i in range(0,n):
            for k in range(i+1,n):
                if arr[i]>arr[k]:
                    arr[i],arr[k]=arr[k],arr[i]
        return arr
# =============================================================================
# =============================================================================
# Insertion sort	https://www.geeksforgeeks.org/problems/insertion-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
def insertionSort(self, alist, n):
    #code here
  for i in range(1, n):

    key = alist[i]

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >= 0 and key < alist[j] :
            alist[j + 1] = alist[j]
            j -= 1
    arr[j + 1] = key

# =============================================================================
# =============================================================================
# Merge sort	https://www.geeksforgeeks.org/problems/merge-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
    def merge(self,arr, l, m, r): 
        # code here
        n1=m-l+1
        n2=r-m
        L=[0]*n1
        R=[0]*n2
        for i in range(n1):
            L[i]=arr[l+i]
        for j in range(n2):
            R[j]=arr[m+1+j]
        i=0
        j=0
        k=l
        while i<n1 and j<n2:
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<n1:
            arr[k]=L[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=R[j]
            j+=1
            k+=1
 
    def mergeSort(self,arr, l, r):
        #code here
        if l<r:
            m=(l+(r-1))//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr,l,m,r)
        return arr
# =============================================================================
# =============================================================================

# Quick sort	https://www.geeksforgeeks.org/problems/quick-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
#User function Template for python3
import random
class Solution:
    def quickSort(self,arr,low,high):
        if low<high:
            p = self.partition(arr,low,high)
            self.quickSort(arr,low,p)
            self.quickSort(arr,p+1, high)
        return
    
    def partition(self,arr,low,high):
        rand = random.randint(low,high)
        pivot = arr[rand]
        arr[low],arr[rand] = arr[rand],arr[low]
        l=low-1
        r=high+1
        while True:
            l+=1
            while arr[l]<pivot:
                l+=1
            r-=1
            while arr[r]>pivot:
                r-=1
            if l>=r:
                return r
            arr[l],arr[r] = arr[r],arr[l]
# # =============================================================================
# =============================================================================
