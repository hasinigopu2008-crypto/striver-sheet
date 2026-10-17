#my approach=optimal approach
import math
class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        for i in range(2,int(math.isqrt(n))+1):
            if n%i==0:
                return False
        return True
#optimal approach 2
import math
class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False   
        # Start checking at 5, and step by 6 to only check 6k-1 and 6k+1
        for i in range(5, math.isqrt(n) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False      
        return True        
