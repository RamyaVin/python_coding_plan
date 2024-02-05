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
        left, right = 0, n - 1
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

    def Reduced_String(self, k, s):
        stack = list()
        crush = False
        for char in s:
            stack.append(char)
            if len(stack) >= k:
                for position in range(1,k+1):
                    if stack[-position] == char:
                        crush = True
                    else:
                        crush = False
                        break
            if crush:
                for _ in range(k):
                    stack.pop()
                crush = False
        return ''.join(stack)

# =============================================================================
# =============================================================================
# 146	Count the reversals	https://www.geeksforgeeks.org/problems/count-the-reversals0401/1?page=1&category=Queue&sortBy=submissions
def countRev (s):
    n = len(s)
    if n % 2 != 0:
        return -1
    left_count = right_count = 0
    for i in range(n):
        if s[i] == '{':
            left_count += 1
        else:
            if left_count == 0:
                right_count += 1
            else:
                left_count -= 1
    return (left_count + 1) // 2 + (right_count + 1) // 2
# =============================================================================
# =============================================================================
# Subtree & Other must do tree probs		
# =============================================================================
# =============================================================================
# Basic patterns and must solve(Each prob in this pattern will teach you something and also as you solve, you will start mastering it though initially it takes sometime)	
#Understand the basics of backtracking and start solving	
# =============================================================================
# =============================================================================
# 147	What is queue? Learn the basic representation and how its implemented?	https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?page=1&category=Queue&sortBy=submissions
Three 90 Challenge Extended On Popular Demand! Don't Miss Out Now 

banner
Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)

class MyQueue:
    def __init__(self):
        self.arr=[]
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.arr:
            return self.arr.pop(0)
        else:
            return -1
# =============================================================================
# =============================================================================
# 148	Implement queue using linkedlist	https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1?page=1&category=Queue&sortBy=submissions
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head=None
        self.tail=None
    #Function to push an element into the queue.
    def push(self, item): 
        newnode=Node(item)
        if self.head is None or self.tail is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=self.tail.next
            
    def pop(self):
        if self.head==None:
            return -1
        else:
            item=self.head.data
            self.head=self.head.next
        return item

# =============================================================================
# =============================================================================
# 149	Implement queue using stack(super imp)	https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1?page=1&category=Queue&sortBy=submissions
def Push(x,stack1,stack2):
    while stack1:
        stack2.append(stack1.pop())
    stack2.append(x)
    while stack2:
        stack1.append(stack2.pop())
#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    if stack1:
        return stack1.pop()
    else: return -1
# =============================================================================
# =============================================================================
# 150	Implement stack using queue(super imp)	https://www.geeksforgeeks.org/problems/stack-using-two-queues/1?page=1&category=Queue&sortBy=submissions
# Function to push an element into stack using two queues.
def push(x):
    global queue_1
    global queue_2
    
    # Adding the new element to queue_2
    queue_2.put(x)
    
    # Moving all elements from queue_1 to queue_2
    while not queue_1.empty():
        queue_2.put(queue_1.get())
        
    # Swapping the names of the queues
    queue_1, queue_2 = queue_2, queue_1

# Function to pop an element from stack using two queues.
def pop():
    global queue_1
    global queue_2
    
    # If queue_1 is empty, return -1
    if queue_1.empty():
        return -1
    
    # Otherwise, remove and return the front element of queue_1
    return queue_1.get()
# =============================================================================
# =============================================================================
# 151	Reverse a queue	https://www.geeksforgeeks.org/problems/queue-reversal/1?page=1&category=Queue&sortBy=submissions
    #Function to reverse the queue.
    def rev(self, q):
        stack = []
        while not q.empty():
            x = q.get()
            stack.append(x)
            
        while stack:
            q.put(stack.pop())
            
        return q
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
