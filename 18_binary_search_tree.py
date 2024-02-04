# =============================================================================
# =============================================================================
# Binary Search Tree(Once the above patterns are covered, BST probs will become easy, but make sure to learn what BST is in general before starting with probs)	Understand what BST is?	
# 141	Insert at bottom of stack	https://www.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1?page=4&category=Stack&sortBy=submissions
def insertAtBottom(self,St,X):
    St.insert(0,X)
    return St
For Input: 
3 4 N, X
2 1 5
Your Output: 
4 2 1 5
# =============================================================================
# =============================================================================
# 142	Reverse a stack	https://www.geeksforgeeks.org/problems/reverse-a-stack/1?page=2&category=Stack&sortBy=submissions
def reverse(self,St): 
        i=0
        j=len(St)-1
        while i<=j:
            St[i],St[j]=St[j],St[i]
            i+=1
            j-=1
        return St
# =============================================================================
# =============================================================================
# 143	Sort stack(Solving above two can give you hint for this)	https://www.geeksforgeeks.org/problems/sort-a-stack/1?page=1&category=Stack&sortBy=submissions
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        def quicksort(arr,left,right):
            if left<right:
                partition_pos = partition(arr,left,right)
                #print(partition_pos,arr)
                quicksort(arr,left,partition_pos-1)
                quicksort(arr,partition_pos+1,right)
                
        def partition(arr,left,right):
            i=left
            j= right-1
            pivot = arr[right]
            
            while i<j:
                while i<right and arr[i]<pivot:
                    i+=1
                while j>left and arr[j]>=pivot:
                    j-=1
                if i<j:
                    arr[i],arr[j]= arr[j],arr[i]
            if arr[i]> pivot:
                arr[i],arr[right] = arr[right],arr[i]
                    
            return i
        quicksort(s,0,len(s)-1)
# =============================================================================
# =============================================================================
# Construct from given		
# =============================================================================
# =============================================================================
# 144	Celebrity problem	https://www.geeksforgeeks.org/problems/the-celebrity-problem/1?page=1&category=Stack&sortBy=submissions
def celebrity(self, M, n):
        while left < right:
            if M[left][right] == 1:
                left += 1
            else:
                right -= 1
        for i in range(n):
            if i != left and (M[left][i] == 1 or M[i][left] == 0):
                return -1 
        return left 
# =============================================================================
# =============================================================================
# 145	Restrictive candy crush	https://www.geeksforgeeks.org/problems/restrictive-candy-crush--141631/1?page=2&category=Stack&sortBy=submissions
# =============================================================================
# =============================================================================
# 146	Count the reversals	https://www.geeksforgeeks.org/problems/count-the-reversals0401/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# Subtree & Other must do tree probs		
# =============================================================================
# =============================================================================
# Basic patterns and must solve(Each prob in this pattern will teach you something and also as you solve, you will start mastering it though initially it takes sometime)	Understand the basics of backtracking and start solving	
# =============================================================================
# =============================================================================
# 147	What is queue? Learn the basic representation and how its implemented?	https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 148	Implement queue using linkedlist	https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 149	Implement queue using stack(super imp)	https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# 150	Implement stack using queue(super imp)	https://www.geeksforgeeks.org/problems/stack-using-two-queues/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 151	Reverse a queue	https://www.geeksforgeeks.org/problems/queue-reversal/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# Traversals & Basic	Understand how graph is represented?	
# =============================================================================
# =============================================================================
# 152	Circular tour	https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 153	First non repeating char in stream	https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 154	Reverse first k elements in queue	https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 155	LRU Cache(super imp)	https://www.geeksforgeeks.org/problems/lru-cache/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 156	Minimum cost of ropes	https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1?page=1&category=Queue&sortBy=submissions
# =============================================================================
# =============================================================================
# 157	Nearly sorted(Learn priority queue for sure)	https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1?page=3&category=Arrays&difficulty=Medium
# Connected component(After traversal, this will be easy to solve)		

# Bipartite		
# =============================================================================
# =============================================================================
# 158	Maximum sum subarray of size k	https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# 159	Count distinct element in every window(Once you understoor handling window size fixed from above prob, this will be easy)	https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1?page=1&category=sliding-window&sortBy=submissions
# =============================================================================
# =============================================================================
# 160	First negative integer in every window of size k(Try to solve on own before looking for soln since you did above topics too already	https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1?page=1&category=sliding-window&sortBy=submissions
# =============================================================================
# =============================================================================
# 161	Maximum of all subarray of size k(Try to solve on own)	https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1?page=1&category=sliding-window&sortBy=submissions
# =============================================================================
# =============================================================================
# 162	Count substring of length k with k-1 distinct elements	https://www.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1?page=1&category=sliding-window&sortBy=submissions
# =============================================================================
# =============================================================================
# 163	Maximum of minimum for every window(Imp)	https://www.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1?page=1&category=sliding-window&sortBy=submissions
# =============================================================================
# =============================================================================
