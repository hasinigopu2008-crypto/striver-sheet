#my approach
class Solution:
    def isArmstrong(self, n: int) -> bool:
        if n == 0:
            return True    
        num = n
        k = len(str(n))
        total_sum = 0
        while n > 0:
            d = n % 10
            total_sum += d ** k
            n = n // 10    
        return total_sum == num
#optimal approach
class Solution:
    def isArmstrong(self, n):
        s = str(n)
        k = len(s)
        return sum(int(digit) ** k for digit in s) == n
