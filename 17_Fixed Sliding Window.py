# =============================================================================
# Fixed Sliding Window(Size of the window will be provided)				
# Variable sliding window(Each prob will teach something in addition to the window so do solve everything)				
# =============================================================================
# =============================================================================

# 125	What is stack? Leam how to represent the data structure and working of it	https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view

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
# 126	Implement 2 stack using array	https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view

#User function Template for python3

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
# 127	Check for balanced paranthesis	https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view

class Solution:
    
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
# 128	Get min from stack in O(1) space and time	https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view

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
# Traversals	Understand the basic of how tree data structure is represented		Best Tutorial link - click to view	
# =============================================================================
# =============================================================================
# 129	Next greater element 	https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 130	Next greater element II	https://leetcode.com/problems/next-greater-element-ii/	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# Basic and Easy patterns(Try to solve these once you learnt traversals)				
# =============================================================================
# =============================================================================
# 131	Next smallest element on left	https://www.geeksforgeeks.org/problems/help-classmates--141631/1?itm_source=geeksforgeeks	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 132	Next smallest element on right	https://www.codingninjas.com/studio/problems/next-smaller-element_1112581	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 133	Stock span problem(Implementation prob - Try to figure out the pattern from above next greater and smaller)	https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 134	Trapping rainwater	https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 135	Maximum rectangular area on histogram(Once next greater and next smallest pattern is covered, this can be solved easily)	https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 136	Max rectangle(Same as above, just a small twist)	https://www.geeksforgeeks.org/problems/max-rectangle/1?page=1&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view
# Path and Distance				
# 137	Infix to postfix	https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1?page=2&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 138	Evaluation of postfix expression	https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1?page=2&category=Stack&sortBy=submissions	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 139	Prefix to postfix	https://practice.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 140	Arithmetic expression evaluation	https://www.codingninjas.com/studio/problems/arithmetic-expression-evaluation_1170517	Best Tutorial link - click to view	Article link-click to view
# =============================================================================
# =============================================================================
# 
# =============================================================================
