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
        if not self.arr: #check if stack is empty
            return -1
        return self.arr.pop()      
# =============================================================================
# =============================================================================
# 126	Implement 2 stack using array	https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1?page=1&category=Stack&sortBy=submissions	
class TwoStacks:
    def __init__(self, n=100):
        self.p1 = 0
        self.p2 = n // 2
        self.twostack = [0] * (n + 1)
        self.size = n

    def push1(self, x):
        self.twostack[self.p1] = x
        self.p1 += 1

    def push2(self, x):
        self.twostack[self.p2] = x
        self.p2 += 1

    def pop1(self):
        if self.p1 == 0:
            return -1
        self.p1 -= 1
        return self.twostack[self.p1]

    def pop2(self):
        if self.p2 == self.size // 2:
            return -1
        self.p2 -= 1
        return self.twostack[self.p2]
# =============================================================================
# =============================================================================
# 127	Check for balanced paranthesis	https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Stack&sortBy=submissions	
   #Function to check if brackets are balanced or not.
def ispar(self, x):
    stack = []
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']
    pairs = {'{': '}', '[': ']', '(': ')'}

    for char in x:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0 or pairs[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0
    #############
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
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        
        # First iteration: find next greater element from left to right
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        # Second iteration: find next greater element from right to left (circular)
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            # For circular array, search again from the beginning
            if i == n - 1:
                for j in range(n):
                    while stack and nums[j] > nums[stack[-1]]:
                        result[stack.pop()] = nums[j]
        
        return result
# =============================================================================
# =============================================================================
# Basic and Easy patterns(Try to solve these once you learnt traversals)				
# =============================================================================
# =============================================================================
# 131	Next smallest element on left	https://www.geeksforgeeks.org/problems/help-classmates--141631/1?itm_source=geeksforgeeks	
        # Return the list
def nextSmallerElements(arr: List[int]) -> List[int]:
    n = len(arr)
    stack = []
    res = [-1] * n

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            res[stack.pop()] = arr[i]
        stack.append(i)

    return res
# =============================================================================
# =============================================================================
# 132	Next smallest element on right	https://www.codingninjas.com/studio/problems/next-smaller-element_1112581	
def nextSmallerElement(arr, n):
    stack = [0]
    res = [-1] * n

    for i in range(1, n):
        while stack and arr[i] < arr[stack[-1]]:
            res[stack.pop()] = arr[i]
        stack.append(i)

    return res
# =============================================================================
# =============================================================================
# 133	Stock span problem(Implementation prob - Try to figure out the pattern from above next greater and smaller)	https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1?page=1&category=Stack&sortBy=submissions	
    #Function to calculate the span of stock price for all n days.
def calculateSpan(self, a, n):
    res = [1] * n
    stack = []

    for i in range(n):
        while stack and a[i] >= a[stack[-1]]:
            res[i] += res[stack.pop()]
        stack.append(i)

    return res
# =============================================================================
# =============================================================================
# 134	Trapping rainwater	https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article	
def trappingWater(self, arr, n):
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

def calculate_trapped_water(self, arr, left_max, right_max, n):
    res = 0
    for i in range(n):
        res += min(left_max[i], right_max[i]) - arr[i]
    return res
arr = [10,0, 9]
# =============================================================================
# =============================================================================
# 135	Maximum rectangular area on histogram(Once next greater and next smallest pattern is covered, this can be solved easily)	https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1?page=1&category=Stack&sortBy=submissions	
    #Function to find largest rectangular area possible in a given histogram.
def getMaxArea(self, histogram):
    stack = []
    res = 0

    for height in histogram + [0]:
        step = 0
        while stack and stack[-1][1] >= height:
            w, h = stack.pop()
            step += w
            res = max(res, step * h)
        stack.append((step + 1, height))

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
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, hist[top] * width)
        while stack:
            top = stack.pop()
            width = i - stack[-1] - 1 if stack else i
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
    stack = []
    output = ''
    operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in exp:
        if char not in operators:
            output += char
        else:
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    output += stack.pop()
                stack.pop()
            elif len(stack) == 0 or operators[char] > operators[stack[-1]]:
                stack.append(char)
            else:
                while len(stack) != 0 and (operators[char] <= operators[stack[-1]] or stack[-1] != '('):
                    output += stack.pop()
                stack.append(char)

    while len(stack) != 0:
        output += stack.pop()

    return output    
# =============================================================================
# =============================================================================
# 138	Evaluation of postfix expression	https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1?page=2&category=Stack&sortBy=submissions	
def evaluatePostfix(self, s):
    stack = []

    for char in s:
        if char in ["+", "*", "/", "-"]:
            y, x = stack.pop(), stack.pop()

            if char == "+":
                stack.append(x + y)
            elif char == "*":
                stack.append(x * y)
            elif char == "-":
                stack.append(x - y)
            else:
                stack.append(x // y)
        else:
            stack.append(int(char))

    return stack[-1]
# =============================================================================
# =============================================================================
# 139	Prefix to postfix   https://www.geeksforgeeks.org/prefix-postfix-conversion/	
s = "*-A/BC-/AKL"
def pre_to_post(s):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    result = []

    # Reversing the order
    s = s[::-1]

    # iterating through individual tokens
    for i in s:
        # if token is operator
        if i in operators:
            # pop 2 elements from stack
            a = stack.pop()
            b = stack.pop()
            # concatenate them as operand1 + operand2 + operator
            temp = a + b + i
            stack.append(temp)
        # else if operand
        else:
            stack.append(i)

    # storing final output in result list
    result = stack[::-1]
    
    # returning final output as a string
    return ' '.join(result)

# =============================================================================
# =============================================================================

# Get Infix for a given postfix  expression 
def getInfix(exp):
    stack = [] 
    for char in exp:              
        # Push operands 
        if isOperand(char):         
            stack.append(char)              
        # We assume that input is a valid postfix and expect an operator. 
        else:         
            op1 = stack.pop() 
            op2 = stack.pop() 
            stack.append("(" + op2 + char + op1 + ")")              
    # There must be a single element in stack now which is the required infix. 
    return stack[0]
 
# Helper function to check if a character is an operand
def isOperand(char):
    return char.isalpha()
 
# Driver Code 
if __name__ == '__main__': 
    exp = "ab*c+"
    print(getInfix(exp.strip()))
###########3
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
            s.insert(0, "(" + op2 + i + op1 + ")")              
    # There must be a single element in     # stack now which is the required     # infix. 
    return s[0]
 
# Driver Code 
if __name__ == '__main__': 
    exp = "ab*c+"
    print(getInfix(exp.strip()))
# =============================================================================
# =============================================================================
#140	Arithmetic expression evaluation	https://www.codingninjas.com/studio/problems/arithmetic-expression-evaluation_1170517
def isLowerPrecedence(ops1, ops2):
    # Check whether ops1 has lower precedence than ops2.
    if (ops1 in ['+', '-']) and (ops2 in ['*', '/']):
        return True
    return False

def evaluateArithmeticExpression(expression):
    stack = []
    postfixExp = ""
    operand = ""
    
    # Convert given infix expression to postfix/ Reverse Polish Notation.
    for char in expression:
        if char.isdigit():
            # Append digit to operand.
            operand += char
        else:
            if operand:
                # Append operand in string 'postfix'
                postfixExp += operand + ' '
                operand = ""
            
            if char == '(':
                # Push opening bracket
                stack.append(char)
            elif char == ')':
                # Append operators between current parenthesis pair in string postfixExp and discard parenthesis.
                while stack[-1] != '(':
                    postfixExp += stack.pop() + ' '
                stack.pop()
            else:
                while stack and stack[-1] != '(' and not isLowerPrecedence(char, stack[-1]):
                    # Pop operator with greater or equal precedence.
                    postfixExp += stack.pop() + ' '
                # Add operator to top of stack.
                stack.append(char)
    
    if operand:
        postfixExp += operand + ' '
    
    # Append remaining operators in stack to postfixExp.
    while stack:
        postfixExp += stack.pop() + ' '
    
    values = []
    operand = ""
    
    # Evaluating equivalent postfix expression.
    for token in postfixExp.strip().split():
        if token.isdigit():
            # Push operand in stack 'values'.
            values.append(int(token))
        else:
            # Pop two operands and push their result after applying operator back to the stack 'values'.
            operand2 = values.pop()
            operand1 = values.pop()
            if token == '+':
                values.append(operand1 + operand2)        
            elif token == '-':
                values.append(operand1 - operand2)            
            elif token == '*':
                values.append(operand1 * operand2)            
            elif token == '/':
                values.append(int(operand1 / operand2))
    
    # Result of Expression
    return values[-1]
#####################
def isLowerPrecedence(ops1, ops2):
    # Check whether ops1 has lower precedence than ops2.
    if((ops1 == '+' or ops1 == '-') and (ops2 == '*' or ops2 == '/')):
        return True
    return False
    
def evaluateArithmeticExpression(expression):
    stk = []
    postfixExp = ""
    operand = ""
    # Convert given infix expression to postfix/ Reverse Polish Notation.
    for i in range(len(expression)):
        if (expression[i] >= '0' and expression[i] <= '9'):
            # Append digit to operand.
            operand += expression[i]
            continue
        if (operand != ""):            
            # Append operand in string 'postfix'
            postfixExp += operand
            postfixExp += ' '
            operand = ""
        if (expression[i] == '('):            
            # Push opening bracket
            stk.append('(')        
        elif (expression[i] == ')'):            
            # Append operators between current paranthesis pair in string postfixExp and discard paranthesis.
            while (stk[-1] != '('):
                postfixExp += stk[-1]
                stk.pop()
            stk.pop()        
        else:
            while (stk[-1] != '(' and isLowerPrecedence(expression[i], stk[-1]) == False):                
                # Pop operator with greater or equal precedence.
                postfixExp += stk[-1]
                stk.pop()

            # Add operator to top of stack.
            stk.append(expression[i])

    values = []
    operand = ""

    # Evaluating equivalent postfix expression.
    for i in range(len(postfixExp)):
        if (postfixExp[i] >= '0' and postfixExp[i] <= '9'):            
            # Append digit to operand.
            operand += postfixExp[i]        
        elif (postfixExp[i] == ' '):            
            # Push operand in stack 'values'.
            values.append(int(operand))
            operand = ""        
        else:            
            # Pop two operand and push their result after applying operator back to the stack 'values'.
            operand2 = values[-1]
            values.pop()
            operand1 = values[-1]
            values.pop()
            if (postfixExp[i] == '+'):
                values.append(operand1 + operand2)        
            if (postfixExp[i] == '-'):
                values.append(operand1 - operand2)            
            if (postfixExp[i] == '*'):
                values.append(operand1 * operand2)            
            if (postfixExp[i] == '/'):
                values.append(int(operand1 / operand2))
    # Result of Expression
    return values[-1]
# =============================================================================
# =============================================================================

