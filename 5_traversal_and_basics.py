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
# =============================================================================
# =============================================================================
# Find triplets with zero sum
# =============================================================================
# =============================================================================
# Find count of triplets
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
