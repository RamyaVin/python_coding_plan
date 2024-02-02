# =============================================================================
# Fixed Sliding Window(Size of the window will be provided)				
# Variable sliding window(Each prob will teach something in addition to the window so do solve everything)				
# =============================================================================
# =============================================================================

# 125	What is stack? Leam how to represent the data structure and working of it	https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?page=1&category=Stack&sortBy=submissions	
class MyStack:    
    def __init__(self):
        self.arr=[]    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if len(self.arr)<1:
            return -1
        return self.arr.pop()      
# =============================================================================
# =============================================================================
# 126	Implement 2 stack using array	https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1?page=1&category=Stack&sortBy=submissions	
class TwoStacks:
    def __init__(self, n=100):
        self.p1=0
        self.p2=n//2
        self.twostack=[0]*(n+1)
        self.size=n
    # Function to push an integer into stack 1
    def push1(self, x):
        self.twostack[self.p1]=x
        self.p1+=1
        pass

    # Function to push an integer into stack 2
    def push2(self, x):
        self.twostack[self.p2]=x
        self.p2+=1
        pass

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.p1==0:
            return -1
        else:
            t=self.twostack[self.p1-1]
            #self.twostack[self.p1-1]=0
            self.p1-=1
            return t
        pass

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.p2==self.size//2:
            return -1
        else:
            
            t=self.twostack[self.p2-1]
            #self.twostack[self.p2-1]=0
            self.p2-=1
            return t
        pass
# =============================================================================
# =============================================================================
# 127	Check for balanced paranthesis	https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Stack&sortBy=submissions	
   #Function to check if brackets are balanced or not.
    def ispar(self,x):
        
       stack = []
       for char in x:
            if char in ['{', '[', '('] :
               stack.append(char)
            else:
                if len(stack) == 0:
                   return False
                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                        continue
                if char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                        continue
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                        continue
                return False
                
       if len(stack):
            return False
       return True
# =============================================================================
# =============================================================================
# 128	Get min from stack in O(1) space and time	https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&category=Stack&sortBy=submissions	
class stack:
    class Node:
        def __init__(self,val,mini):
            self.val = val
            self.mini = mini
    def __init__(self):
        self.s=[]
        self.minEle= None

    def push(self,x):
        #CODE HERE
        if not self.s:
            self.s.append(self.Node(x,x))
            #print(x,x)
        else:
            self.minEle = min(self.s[-1].mini,x)
            self.s.append(self.Node(x,self.minEle))
            #print(x,self.minEle)

    def pop(self):
        #CODE HERE
        if self.s:
            return self.s.pop().val
        else:
            return -1
           
    def getMin(self):
        #CODE HERE
        if self.s:
            return self.s[-1].mini
        else:
            return -1
# =============================================================================
# =============================================================================
# Traversals	Understand the basic of how tree data structure is represented			
# =============================================================================
# =============================================================================
# 129	Next greater element 	https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1?page=1&category=Stack&sortBy=submissions	
    def nextLargerElement(self,arr,n):
        stack = [0]
        res = [None]*n
        i=1
        #print(res)
        while(i<n):
            while(stack and arr[i]>arr[stack[-1]]):
                res[stack.pop()]=arr[i]
            stack.append(i)
            i=i+1
        while(stack):
            res[stack.pop()]=-1
        return res
# =============================================================================
# =============================================================================
# 130	Next greater element II	https://leetcode.com/problems/next-greater-element-ii/	

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []
        ans = [-1] * n
        for i in range(n * 2 - 1, -1, -1):
            while st and st[-1] <= nums[i % n]:
                st.pop()
            if i < n:
                ans[i] = st[-1] if st else -1
            st.append(nums[i % n])
        return ans
# =============================================================================
# =============================================================================
# Basic and Easy patterns(Try to solve these once you learnt traversals)				
# =============================================================================
# =============================================================================
# 131	Next smallest element on left	https://www.geeksforgeeks.org/problems/help-classmates--141631/1?itm_source=geeksforgeeks	
        # Return the list
        stack = []
        res = [-1]*n
        for i in range(n):
            while(stack and arr[i] < arr[stack[-1]]):
                res [stack.pop()]=arr[i]
            stack.append(i)
        return res
# =============================================================================
# =============================================================================
# 132	Next smallest element on right	https://www.codingninjas.com/studio/problems/next-smaller-element_1112581	
def nextSmallerElement(arr,n):
    # Write your code here.
    pass
    
    stack = [0]
    res = [None]*n
    i=1
    #print(res)
    while(i<n):
        while(stack and arr[i]<arr[stack[-1]]):
            res[stack.pop()]=arr[i]
        stack.append(i)
        i=i+1
    while(stack):
        res[stack.pop()]=-1
    return res
# =============================================================================
# =============================================================================
# 133	Stock span problem(Implementation prob - Try to figure out the pattern from above next greater and smaller)	https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1?page=1&category=Stack&sortBy=submissions	
    #Function to calculate the span of stock price for all n days.
    def calculateSpan(self,a,n):
        res = [1]*n
        stack = []
        for i in range(n):
            while(stack and a[i]>=a[stack[-1]]):
                res [i] = res[i]+res[stack.pop()]
            stack.append(i)
        return res
# =============================================================================
# =============================================================================
# 134	Trapping rainwater	https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article	

    def trappingWater(self, arr,n):
        if n <= 1:
            return 0
            
        left_max = self.calculate_left_max(arr, n)
        right_max = self.calculate_right_max(arr, n)
        
        return self.calculate_trapped_water(arr, left_max, right_max, n)
        
    def calculate_left_max(self, arr, n):
            left_max = [0] * n
            left_max[0] = arr[0]
            
            for i in range(1, n):
                left_max[i] = max(left_max[i-1], arr[i])
            
            return left_max
            
    def calculate_right_max(self, arr, n):
            right_max = [0] * n
            right_max[n-1] = arr[n-1]
            
            for i in range(n-2, -1, -1):
                right_max[i] = max(right_max[i+1], arr[i])
            
            return right_max
        
    def calculate_trapped_water(self,arr,left_max,right_max,n):
            res = 0
            
            for i in range(n):
                res += min(left_max[i], right_max[i]) - arr[i]
            return res
arr = [10,0, 9]
# =============================================================================
# =============================================================================
# 135	Maximum rectangular area on histogram(Once next greater and next smallest pattern is covered, this can be solved easily)	https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1?page=1&category=Stack&sortBy=submissions	
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        st, res = [], 0
        for height in histogram + [0]:
            step = 0
            while st and st[-1][1] >= height:
                w, h = st.pop()
                step += w
                res = max(res, step * h)
            st.append((step + 1, height))
        return res
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
# =============================================================================
# =============================================================================
# 136	Max rectangle(Same as above, just a small twist)	https://www.geeksforgeeks.org/problems/max-rectangle/1?page=1&category=Stack&sortBy=submissions	

def maxArea(self, M, n, m):
        def maxHistArea(hist):
            stack = []
            max_area = 0
            i = 0
            while i < m:
                if not stack or hist[stack[-1]] <= hist[i]:
                    stack.append(i)
                    i += 1
                else:
                    top = stack.pop()
                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i
                    max_area = max(max_area, hist[top] * width)
            while stack:
                top = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, hist[top] * width)
            return max_area
        for i in range(1, n):
            for j in range(m):
                if M[i][j] == 1:
                    M[i][j] += M[i - 1][j]
        max_area = 1
        for i in range(n):
            max_area = max(max_area, maxHistArea(M[i]))
        return max_area
# Path and Distance				
# 137	Infix to postfix	https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1?page=2&category=Stack&sortBy=submissions	
Input: str = "A*(B+C)/D"
Output: ABC+*D/
    def InfixtoPostfix(self, exp):
        s=[]
        out=''
        op={'(':0,')':0,'+':1,'-':1,'*':2,'/':2,'^':3}
        for i in exp:
            if i not in op.keys():
                out=out+i
            else:
                if i=='(': s.append(i)
                elif i==')':
                    while s[-1]!='(':
                        out=out+s.pop()
                    s.pop()
                elif len(s)==0 or op[i]>op[s[-1]]:
                    s.append(i)
                else:
                    while len(s)!=0 and (op[i]<=op[s[-1]] or s[-1]!='('):
                        out=out+s.pop()
                    s.append(i)
        while len(s)!=0:
            out=out+s.pop()
        return out             
# =============================================================================
# =============================================================================
# 138	Evaluation of postfix expression	https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1?page=2&category=Stack&sortBy=submissions	
    def evaluatePostfix(self, s):
        stack=[]
        for i in s:
            if i in ["+","*","/","-"]:
                y,x=stack.pop(),stack.pop()
                if i=="+":stack.append(x+y)
                elif i=="*":stack.append(x*y)
                elif i=="-":stack.append(x-y)
                else:stack.append(x//y)
            else:stack.append(int(i))
        return stack[-1]
# =============================================================================
# =============================================================================
# 139	Prefix to postfix	https://www.geeksforgeeks.org/postfix-to-infix/	
# Python3 program to find infix for  a given postfix. 
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z')) 
 
# Get Infix for a given postfix  expression 
def getInfix(exp) :
    s = [] 
    for i in exp:              
        # Push operands 
        if (isOperand(i)) :         
            s.insert(0, i) 
             
        # We assume that input is a valid postfix and expect  an operator. 
        else:         
            op1 = s[0] 
            s.pop(0) 
            op2 = s[0] 
            s.pop(0) 
            s.insert(0, "(" + op2 + i +
                             op1 + ")") 
             
    # There must be a single element in     # stack now which is the required     # infix. 
    return s[0]
 
# Driver Code 
if __name__ == '__main__': 
    exp = "ab*c+"
    print(getInfix(exp.strip()))
# =============================================================================
# =============================================================================
# 140	Arithmetic expression evaluation	https://www.codingninjas.com/studio/problems/arithmetic-expression-evaluation_1170517	
# =============================================================================
# =============================================================================
# 
# =============================================================================
