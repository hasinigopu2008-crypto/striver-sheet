#my approach
class Solution:
    def reverseNumber(self, n):
        result=0
        while n>0:
            d=n%10
            n=n//10
            result=result*10+d
        return result
#optimal approach
class Solution:
    def reverseNumber(self, n):
        sign = -1 if n < 0 else 1
        reversed_str = str(abs(n))[::-1]
        return sign * int(reversed_str)
