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


# =============================================================================
# =============================================================================
# Sort an array of 0s , 1s and 2s (You dont need to know any sorting algo, just using basics, once solved, definitely learn the optimal algo)

# =============================================================================
# =============================================================================
# Check if two arrays are equal or not
# =============================================================================
# =============================================================================
# Rotate the array by 1
# =============================================================================
# =============================================================================
# Rotate the array by k
# =============================================================================
# =============================================================================
# Array subset of another array
# =============================================================================
# =============================================================================
# Learn what is map and how its represented before moving forward
# =============================================================================
# =============================================================================
# Count frequency of elements in array(Solve efficiently, try applying what you learnt about map)
# =============================================================================
# =============================================================================

