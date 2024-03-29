# =============================================================================
# 64	Search element in sorted rotated array(With and without duplicate)	https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
########33leetcode best########
def search(self, nums, target):
	if target in nums:
		    return True
		else:
		    return False
#################
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
 ### without sort ########3if time is there check
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
arr.sort()
return arr[0]
# =============================================================================
# =============================================================================
# 66	Number of times array is sorted	https://www.geeksforgeeks.org/problems/rotation4723/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
def findKRotation(arr, n):
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
def findMaximum(arr,low,high):
    max = arr[low]
    i = low
    for i in range(high+1):
        if arr[i] > max:
            max = arr[i]
    return max
 
# Driver program to check above functions */
arr = [1, 30, 40, 50, 60, 70, 23, 20]
n = len(arr)
print ("The maximum element is %d"%
        findMaximum(arr, 0, n-1))
