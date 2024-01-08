# =============================================================================
# Find even or odd
class Solution:
    def evenOdd(x):
        if x%2 ==1: return "Odd"
        else: return "Even"
        
print(Solution.evenOdd(4))
# =============================================================================
# =============================================================================
# Find last digit in a number
class Solution:
    def lastDigit(x):
        return abs(x%10)
        
print(Solution.lastDigit(40190))
# =============================================================================
# =============================================================================
# Count digits in a number(Solving above last digit prob wil make this easy for you)
class Solution:
    def countDigits(x):
        count=0
        while x!=0:
            x//=10
            count+=1
        return count

print(Solution.countDigits(4090))
# =============================================================================
# =============================================================================
# Reverse a number(Try thinking how you can use above logic in solving this)
class Solution():
    def reverse( x):
        if x > 2 ** 31 - 1 or x < -(2 ** 31):
            return 0
        
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10
        result = sign * reverse
        return result
    
Solution.reverse(345345601)
# =============================================================================
# =============================================================================
# Find power of a number
#12**21/(10**9+7)
class Solution():
    def powerOfNumber( x):
        if x > 2 ** 31 - 1 or x < -(2 ** 31):
            return 0
        
        reverse = 0
        sign = -1 if x < 0 else 1
        temp=x
        x = abs(x)
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10
        result = sign * reverse
        mod=10**9 + 7
        print(temp,result,mod)
        return print(pow(temp,result,mod))
    
    
Solution.powerOfNumber(12)

# =============================================================================
# =============================================================================
# GCD
class Solution():
    def GCD(a,b):
        rem=1
        if a > b:
            dividend=a
            divisor=b
        else: 
            dividend=b
            divisor=a
        while rem!=0:
            rem=dividend%divisor
            if rem!=0:
                dividend=divisor
                divisor=rem
        return divisor             
            
Solution.GCD(120,40)

# =============================================================================
# =============================================================================
# Print all divisors of a number
class Solution():
    def sum_divs(n):
        i = 1
        s=[]
        while i <= n//2 : 
            if (n % i==0) : 
                s.append(i)
            i+=1
        s.append(n)
        return s
                         
Solution.sum_divs(45)
# =============================================================================
# =============================================================================
# Prime number(Try solving by yourself)
class Solution():
    def prime(n):
        flag=0
        for i in range(2, n//2, 1 ): 
            if (n%i==0): 
                flag=1               
                break
        if flag==1: print("Not Prime")
        else: print("Prime")
        return
    
Solution.prime(139)
# =============================================================================
# =============================================================================
# Armstrong number(Solving power of number, will make this easy for you)
class Solution():
    def armstrong(n):
        result=0
        digits=len(str(n))
        for i in range(1, n): 
            result=result+(n%10)**(digits)
            n=n//10
        return result
    
Solution.armstrong(123)
# =============================================================================
# =============================================================================
# Check palindrome of number(Use the techniques you learnt so far solving above probs and solve this by yourself)
class Solution():
    def palindrome(n):
        x=str(n)
        if x==x[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome" 
    
Solution.palindrome(100)
# also palindrom of negative number 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        div = 1
        while x >= 10 * div:
            div*=10

        while x:
            if x // div != x % 10:return False 
            x = (x % div) // 10 
            div = div/100

        return True
# =============================================================================
# =============================================================================
# Square root of a number(Try to first figure out algo to solve this)
class Solution():
    def squareRoot(n):
        if n>0: flag=1
        else: flag=-1
        return flag*(abs(n)**(1/2) )
    
Solution.squareRoot(-100)
# =============================================================================
# =============================================================================
# Perfect number
class Solution():
    def perfectNumber(n):
        total=0
        for i in range(1,n//2+1):
            if n%i==0: 
                total=total+i
                print(i,"i")
                print(total,"total")
            else: 
                i+=1
        print(total)
        if total == n:
            print(n , "is a perfect number")
            return "Perfect number" 
        else: 
            return "Not perfect number"
    
Solution.perfectNumber(61)
# =============================================================================
