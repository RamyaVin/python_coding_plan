# =============================================================================
# Selection sort	https://www.geeksforgeeks.org/problems/selection-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
#f O(n^2), where n is the length of the array. This is because the algorithm requires nested loops to iterate through the array and perform comparisons and swaps.
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
  for i in range(1, n):
    key = alist[i]
    # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
    j = i-1
    while j >= 0 and key < alist[j] :
            alist[j + 1] = alist[j]
            j -= 1
    arr[j + 1] = key
# =============================================================================
# =============================================================================
# Merge sort	https://www.geeksforgeeks.org/problems/merge-sort/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
    def merge(self,arr, l, m, r): 
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
# O(n log n), where n is the length of the array. However, the worst-case time complexity can be O(n^2) if the pivot selection is not optimal. The use of random pivot selection helps to mitigate this issue.
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
