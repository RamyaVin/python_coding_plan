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
# =============================================================================
# =============================================================================
# 60	Find first and last occurence of element in sorted array	https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1?page=1&category=Binary%20Search&sortBy=submissions
# =============================================================================
# =============================================================================
# 61	Find missing num from 1 to N	https://leetcode.com/problems/missing-number/
# =============================================================================
# =============================================================================
# 62	Find square root	https://www.geeksforgeeks.org/problems/square-root/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# 63	Search for element in infinite array	https://www.codingninjas.com/studio/problems/search-in-infinite-sorted-0-1-array_696193
# 
# =============================================================================
