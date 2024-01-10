# =============================================================================
# What is an array? How is it represented?
# =============================================================================
# =============================================================================
# Find the maximum and minimum element in array(After solving the search , you can solve all probs in this basics by yourself)
class Solution():
    def maxMinArray(s):
        max_array=s[0]
        min_array=s[0]
        for i in range(0,len(s),1):
            max_array=max(max_array,s[i])
            min_array=min(min_array,s[i])
        return  max_array,min_array

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
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        if k == 0:
            return nums
        if len(nums)<k:
            nums[:] = Solution.rorateArray_k(nums,len(nums))
            nums[:] = Solution.rorateArray_k(nums,k-len(nums))
 
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

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
# =============================================================================
# =============================================================================

