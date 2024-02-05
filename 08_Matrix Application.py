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
"""
Use a memoization dictionary: As the factorial function is recursive, it can result in redundant calculations when the same factorial is computed multiple times. By using a memoization dictionary, you can store previously calculated factorials and avoid redundant calculations. This can greatly improve the performance of the code, especially for larger values of n.
Use a helper function for memoization: Instead of modifying the factorial function directly, you can create a separate helper function that handles the memoization logic. This allows the factorial function to remain focused on the computation logic, while the helper function takes care of caching the results.
In terms of time complexity, the optimized code has a time complexity of O(n), where n is the given number for which the factorial is computed. This is because the code performs a recursive computation for each value from n down to 0, and the result for each value is stored in the memoization dictionary for future use. Subsequent calls for the same value of n can be directly retrieved from the memoization dictionary, resulting in constant time lookup.
The space complexity of the optimized code is O(n) as well, due to the memoization dictionary. In the worst case, the dictionary could store factorials for each value from n down to 0, resulting in a space complexity proportional to n."""
class Solution:
    def factorial(self, n):
        memo = {}  # Memoization dictionary
        
        def factorial_helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                result = 1
            else:
                result = n * factorial_helper(n - 1)
            memo[n] = result  # Store the computed factorial
            return result
        return factorial_helper(n)
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
"""
Use memoization: Similar to the factorial function discussed earlier, the Fibonacci function can benefit from memoization to avoid redundant calculations. By using a memoization dictionary, you can store previously calculated Fibonacci numbers and retrieve them directly when needed.
Use a helper function for memoization: As with the factorial function, it is recommended to create a separate helper function that handles the memoization logic. This allows the Fibonacci function to focus on the computation logic, while the helper function takes care of caching the results."""
class Solution:
    def fib(self, n):
        memo = {}  # Memoization dictionary
        
        def fib_helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                result = 0
            elif n == 1 or n == 2:
                result = 1
            else:
                result = fib_helper(n - 1) + fib_helper(n - 2)
            memo[n] = result  # Store the computed Fibonacci number
            return result
        
        return fib_helper(n)
# =============================================================================
# =============================================================================
# 54	Power(x,n) Draw the recursion tree for all the probs for sure	https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

#User function Template for python3
#O(log R), as it performs repeated squaring to compute the power. The time complexity of the code is therefore dependent on the time complexity of the pow() function.
#The space complexity of the code is O(1) since it does not utilize any additional data structures that grow with the input size.
class Solution:
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
#using list comprehension and the range() function.
def pattern(N):
    if N <= 0:
        return [N]
    return [i for i in range(N, -5, -5)] + [i for i in range(-5, N, 5)]
# =============================================================================
# =============================================================================
# 56	Recursive implementation of atoi	https://practice.geeksforgeeks.org/problems/implement-atoi/1?utm_source=geeksforgeeks&utm_medium=ml_Article_practice_tab&utm_campaign=Article_practice_tab
#Both approaches appear to be correct, but the second approach provides more control over the conversion process and allows for handling specific cases. The first approach relies on the exception handling mechanism to determine if the conversion is possible.
#In terms of time complexity, both approaches have a time complexity of O(N), where N is the length of the string. This is because both approaches iterate over the characters of the string to perform checks or conversion operations.
#The space complexity of both approaches is O(1) since they do not utilize any additional data structures that grow with the input size.
############
def atoi(string):
      try:
            return int(string)
        except:
            return -1
################
def atoi(string):
        if string[0]=='-':
            if all(c.isdigit() for c in string[1:]):
                return int(string)
        elif all(c.isdigit() for c in string):
            return int(string)
        return -1
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
##########
"""Use memoization
Use a helper function for memoization
In terms of time complexity, the optimized code has a time complexity of O(n^2), where n is the given row number for which Pascal's Triangle is computed. This is because the code performs a recursive computation for each row from n down to 1, and for each row, it calculates the sum of adjacent elements. The time complexity of each row calculation is proportional to the number of elements in the row, which is roughly n.
The space complexity of the optimized code is O(n^2) as well, due to the memoization dictionary. In the worst case, the dictionary could store rows of Pascal's Triangle for each row from n down to 1, resulting in a space complexity proportional to n^2."""
class Solution:
    def nthRowOfPascalTriangle(self, n):
        memo = {}  # Memoization dictionary
        def pascal_helper(n):
            if n in memo:
                return memo[n]
            if n == 1:
                result = [1]
            elif n == 2:
                result = [1, 1]
            else:
                result = [1]
                prev_row = pascal_helper(n - 1)
                for i in range(len(prev_row) - 1):
                    result.append((prev_row[i] + prev_row[i + 1]) % (10**9 + 7))
                result.append(1)
            memo[n] = result  # Store the computed row
            return result
        return pascal_helper(n)
# =============================================================================
