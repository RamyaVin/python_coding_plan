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
