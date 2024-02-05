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
#Three 90 Challenge Extended On Popular Demand! Don't Miss Out Now 

#banner
#Implement a Queue using an Array. Queries in the Queue are of the following type:
#(i) 1 x   (a query of this type means  pushing 'x' into the queue)
#(ii) 2     (a query of this type means to pop element from queue and print the poped element)

class MyQueue:
    def __init__(self):
        self.arr=[]
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
     
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
#Function to find starting point where the truck can start to get through
#the complete circle without exhausting its petrol in between.
def tour(self,lis, n):
    #Code here
    total_petrol, left_petrol = 0, 0
    start = 0
    for i, (p, d) in enumerate(lis):
        tmp = p - d
        total_petrol += tmp
        left_petrol += tmp
        if left_petrol < 0:
            start = i + 1
            left_petrol = 0
    if total_petrol < 0 or start >= n:
        return -1
    return start
# =============================================================================
# =============================================================================
# 153	First non repeating char in stream	https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1?page=1&category=Queue&sortBy=submissions
import sys
class Solution:
	def FirstNonRepeating(self, A):
        n = len(A)
        d = dict()
        
        ans = ""
        
        for i in range(n):
            c = A[i]
            
            if c not in d:
                d[c] = (1, i)
            else:
                count = d[c][0] + 1
                d[c] = ((count, i))
               
            pos = sys.maxsize
            temp = "#"
            
            for it in d:
                if d[it][0] == 1 and d[it][1] < pos:
                    temp = it
                    pos = d[it][1]
           
            ans += temp
        
        return ans
################User function Template for python3
from collections import defaultdict, deque

class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        result = []
        frequency = defaultdict(int)
        queue = deque()
        
        for char in A:
            frequency[char] += 1
            queue.append(char)
            
            while queue and frequency[queue[0]] > 1:
                queue.popleft()
            
            if queue:
                result.append(queue[0])
            else:
                result.append('#')
        
        return ''.join(result)

################

from collections import OrderedDict

class Solution:
    def FirstNonRepeating(self, A):
        charCounter = {}
        charOrder = OrderedDict()
        strLen = len(A)
        res = ''
        
        for i in range(strLen):
            if not A[i] in charCounter:
                charCounter[A[i]] = 1
                charOrder[A[i]] = 0
                res += list(charOrder.keys())[0]
            else:
                charCounter[A[i]] += 1
                
                if charCounter[A[i]] > 1 and A[i] in charOrder:
                    del charOrder[A[i]]
                    
                res += list(charOrder.keys())[0] if list(charOrder.keys()) else '#'
        
        return res



# =============================================================================
# =============================================================================
# 154	Reverse first k elements in queue	https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1?page=1&category=Queue&sortBy=submissions
#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        size = len(q)
        arr = []
        for i in range(k):
            arr.append(q.popleft())
        for i in range(k):
            q.appendleft(arr[i])
            
        return q
# =============================================================================
# =============================================================================
# 155	LRU Cache(super imp)	https://www.geeksforgeeks.org/problems/lru-cache/1?page=1&category=Queue&sortBy=submissions
# design the class in the most optimal way
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.capacity=cap
        self.map={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def insert(self,node):
        self.map[node.key]=node
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head
        
    def remove(self,node):
        del self.map[node.key]
        node.prev.next=node.next
        node.next.prev=node.prev
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.map:
            node=self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        #code here
        if key in self.map:
            self.remove(self.map[key])
        if len(self.map)==self.capacity:
            self.remove(self.tail.prev)
        self.insert(Node(key,value))
# =============================================================================
# =============================================================================
# 156	Minimum cost of ropes	https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1?page=1&category=Queue&sortBy=submissions
#User function Template for python3
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        heapq.heapify(arr)
        ans = 0
        while n>1:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            res = a+b
            heapq.heappush(arr,res)
            ans += res
            n-=1
        return ans
# =============================================================================
# =============================================================================
# 157	Nearly sorted(Learn priority queue for sure)	https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1?page=3&category=Arrays&difficulty=Medium
# Connected component(After traversal, this will be easy to solve)		
from heapq import heappush,heappop
class Solution:
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        heap=[]
        v=[]
        for i in a:
            heappush(heap,i)
            if len(heap)>k:
                v.append(heap[0])
                heappop(heap)
        while len(heap)!=0:
            v.append(heap[0])
            heappop(heap)
        return v
# Bipartite		
# =============================================================================
# =============================================================================
# 158	Maximum sum subarray of size k	https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
    def maximumSumSubarray (self,K,Arr,N):
        # for i in range(N)
        f=sum(Arr[:K])
        cur=f
        for i in range(K,N):
            cur=cur+(Arr[i]-Arr[i-K])
            f=max(f,cur)
        return f
# =============================================================================
# =============================================================================
# 159	Count distinct element in every window(Once you understoor handling window size fixed from above prob, this will be easy)	https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1?page=1&category=sliding-window&sortBy=submissions
Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
    
    def countDistinct(self, A, N, K):
        k_set = set()
        freq = {}
        res = []
        left = 0
        
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0)+1
        res.append(len(freq))
        
        for i in range(k, n):
            freq[arr[i]] = freq.get(arr[i], 0)+1
            freq[arr[left]] = freq[arr[left]]-1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            res.append(len(freq))
            left += 1
        
        return res
# =============================================================================
# =============================================================================
# 160	First negative integer in every window of size k(Try to solve on own before looking for soln since you did above topics too already	https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1?page=1&category=sliding-window&sortBy=submissions
def printFirstNegativeInteger( arr, n, k):
    i=0
    j=0
    ans=[]
    q=[]
    while(j<n):
        if(arr[j]<0):
            q.append(arr[j])
        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            if(len(q)==0):
                ans.append(0)
            else:
                ans.append(q[0])
                if(arr[i]==q[0]):
                    q.pop(0)
            i+=1
            j+=1
    return ans
# =============================================================================
# =============================================================================
# 161	Maximum of all subarray of size k(Try to solve on own)	https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1?page=1&category=sliding-window&sortBy=submissions
import collections
class Solution:
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        output = []
        queue = collections.deque() #(num, index)
        i = 0
        for j in range(n):
            if queue:
                if queue[-1][0] < arr[j]:
                    while queue and queue[-1][0] < arr[j]:
                        queue.pop()
            queue.append((arr[j], j))
            
            if j-i+1>k:
                if queue[0][1] == i:
                    queue.popleft()
                i += 1
            
            if j-i+1==k:
                if queue:
                    output.append(queue[0][0])
                    
        return output
        return ans
# =============================================================================
# =============================================================================
# 162	Count substring of length k with k-1 distinct elements	https://www.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1?page=1&category=sliding-window&sortBy=submissions
    def countOfSubstrings(self, arr, k):
        n=len(arr)
        d={}
        res=0
        f=0
        for r in range(n):
            if arr[r] not in d:
                d[arr[r]]=0
            d[arr[r]]+=1
            if r-f+1>k:
                d[arr[f]]-=1
                if d[arr[f]]==0:
                    del d[arr[f]]
                f+=1
            if r-f+1==k:
                if len(d)==k-1:
                    res+=1
        return res
# =============================================================================
# =============================================================================
# 163	Maximum of minimum for every window(Imp)	https://www.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1?page=1&category=sliding-window&sortBy=submissions
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,N):
        left = [-1] * N
        right = [N] * N
        stack = []
    
        for i in range(N):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
    
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
    
        result = [0] * (N + 1)
        for i in range(N):
            length = right[i] - left[i] - 1
            result[length] = max(result[length], arr[i])
    
        for i in range(N - 1, 0, -1):
            result[i] = max(result[i], result[i + 1])
    
        return result[1:]
# =============================================================================
# =============================================================================
