#my approach
class Solution:
    def countOddDigit(self, n):
        oddCount=0
        while n>0:
            d=n%10
            n=n//10
            if d%2!=0:
                oddCount+=1
        return oddCount
#optimal approach
class Solution:
    def countOddDigit(self, n):
        return sum(1 for d in str(abs(n)) if int(d) % 2 != 0)
