# =============================================================================
# 51	Print 1 to N using recursion	https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1
class Solution:    
    def printNos(self,n):
        #Your code here
        if n==0:
            return 1
        else:
            
            self.printNos(n-1)
            print(n,end=" ")
            
Solution.printNos()
# =============================================================================
# =============================================================================
# 52	Factorial of N numbers	https://practice.geeksforgeeks.org/problems/factorial5739/1
class Solution:    
    def factorial(self,n):
        if n==0: return 1
        else: 
            return(n*self.factorial(n-1))
            
# =============================================================================
# =============================================================================
# 53	Fibonacci series using recursion	https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

class Solution:
    def nthFibonacci(self, n : int) -> int:
        a=0
        b=1
        mod=1000000007
        for i in range(1,n):
            c=(a+b)%mod
            a=b
            b=c
            
        return c
### with recursion 
# Python code to implement Fibonacci series

# Function for fibonacci
def fib(n):

	# Stop condition
	if (n == 0):
		return 0

	# Stop condition
	if (n == 1 or n == 2):
		return 1

	# Recursion function
	else:
		return (fib(n - 1) + fib(n - 2))


# Driver Code

# Initialize variable n.
n = 5;
print("Fibonacci series of 5 numbers is :",end=" ")

# for loop to print the fibonacci series.
for i in range(0,n): 
	print(fib(i),end=" ")

# =============================================================================
# =============================================================================
# 54	Power(x,n) Draw the recursion tree for all the probs for sure	https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        
        return pow(N,R,1000000007)
# =============================================================================
# =============================================================================
# 55	Print pattern	https://www.geeksforgeeks.org/problems/print-pattern3549/1?page=1&category=Recursion&difficulty=Easy&sortBy=submissions

def pattern(N):
    # code here
    if N <= 0:
        return [N,]
    
    a = list(range(N, -5, -5))
    return a + a[::-1][1:]
pattern(16)

# =============================================================================
# =============================================================================
# 56	Recursive implementation of atoi	https://practice.geeksforgeeks.org/problems/implement-atoi/1?utm_source=geeksforgeeks&utm_medium=ml_Article_practice_tab&utm_campaign=Article_practice_tab

##
def atoi(string):
      try:
            return int(string)
        except:
            return -1
##
def atoi(string):
        if string[0]=='-':
            if all(c.isdigit() for c in string[1:]):
                return int(string)
        elif all(c.isdigit() for c in string):
            return int(string)
        return -1
        # Code here
        
atoi("-123a")

# =============================================================================
# =============================================================================
# 57	Pascal triangle	https://www.geeksforgeeks.org/problems/pascal-triangle0652/1?page=1&category=Recursion&difficulty=Easy&sortBy=submissions
 def nthRowOfPascalTriangle(n):
        # code here
        if n==1:
            return([1])
        if n==2:
            return([1,1])
        l=[1]
        k=nthRowOfPascalTriangle(n-1)
        for i in range(len(k)-1):
            l.append((k[i]+k[i+1])%(10**9 +7))
        l.append(1)
        return(l)
    
nthRowOfPascalTriangle(10)
# =============================================================================
