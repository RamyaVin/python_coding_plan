
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
# # =============================================================================
# =============================================================================
