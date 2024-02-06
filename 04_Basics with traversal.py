# =============================================================================
# What is an array? How is it represented?
# =============================================================================
# =============================================================================
# Find the maximum and minimum element in array(After solving the search , you can solve all probs in this basics by yourself)
class Solution():
    def maxMinArray(s):
        max_array = float('-inf')
        min_array = float('inf')
        for i in range(n):
            max_array=max(max_array,s[i])
            min_array=min(min_array,s[i])
        return  min_array,max_array 

Solution.maxMinArray([11,2,3,4,21])

# =============================================================================
# =============================================================================
# Find third largest element in array
#sorted() function has a time complexity of O(n log n).
#O(n)
def max3Array(s):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')

    for num in s:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

    return max3
# =============================================================================
# =============================================================================
# Search an element in array(Understand how to traverse through the array and how to access the elements)
class Solution():
    def search(self,s, n, x):
        n = len(s)
        flag=-1
        for i in range(n):
            if s[i]==x:
                flag=i
                break
                #print("Number in array at location", i )
        return flag
Solution.Array([11,2,3,4,21],3)
# =============================================================================
# =============================================================================
# Find missing number in array
class Solution(object):
    def missingNumber(self, nums, n):
        return ((n * (n+1)) // 2 ) - sum(nums)
# =============================================================================
# =============================================================================
# Find repeating number in array
def repeatingNumber(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return num
        num_set.add(num)
#########
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
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums
    
Solution.sortArray([0,2,1,2,0,1])

# =============================================================================
# =============================================================================
# Check if two arrays are equal or not
class Solution():
    def check(self,x,y,n):
        if len(A) != len(B):
            return 0
        count = {}
        for i in A:
            count[i] = count.get(i, 0) + 1
        for i in B:
            if count.get(i, 0) == 0:
                return 0
            else:
                count[i] -= 1
        return 1
    
Solution.equalArray([1,2,1,2,0,1],[1,2,1,2,0])
# =============================================================================
# =============================================================================
# Rotate the array by 1
#Add the @staticmethod decorator: Since the equalArray method does not access any instance variables or methods, 
#it can be decorated with the @staticmethod decorator to indicate that it is a static method.
def rotate(nums, k):
    #return [nums[-1]] + nums[:-1] gives expected result in python but code not accepting in gfg
    return nums.insert(0, nums.pop())
Solution.rorateArray_1([3,2,1,2,0,1])
# =============================================================================
# =============================================================================
# Rotate the array by k
class Solution(object):
    def rotate(self, nums, k):
        return arr[k:] + arr[:k]
# =============================================================================
# =============================================================================
# Array subset of another array
from collections import Counter
def isSubset( a, b, n, m):
    counter_a = Counter(a)
    counter_b = Counter(b)

    if counter_b - counter_a:
        return "No"
    else:
        return "Yes"
############
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
def frequencyCount(self, arr, N, P):
        N = len(arr)
        freq = [0] * N
    
        for num in arr:
            if 1 <= num <= N:
                freq[num-1] += 1
    
        for i in range(N):
            arr[i] = freq[i]
    
        return arr
################
# Count frequency of elements in array(Solve efficiently, try applying what you learnt about map)
from collections import Counter
def frequencyCount(self, arr):
    return Counter(arr)
    
##################    
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
