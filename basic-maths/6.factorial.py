#my approach
class Solution:
    def factorial(self, n):
        if n==1 or n==0:
            return 1
        return n*self.factorial(n-1)
#optimal approach
class Solution:
    def factorial(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
