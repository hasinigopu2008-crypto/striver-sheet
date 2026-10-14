#my approach
class Solution:
    def largestDigit(self, n):
        n=str(n)
        max=n[0]
        for i in range(len(n)):
            if n[i]>max:
                max=n[i]
        return max
#one-line code
class Solution:
    def largestDigit(self, n):
        return int(max(str(abs(n))))
#optimal approach
class Solution:
    def largestDigit(self, n):
        # Handle negative numbers
        n = abs(n)
        
        # If the number is 0, the largest digit is 0
        if n == 0:
            return 0
            
        max_digit = 0
        while n > 0:
            digit = n % 10
            if digit > max_digit:
                max_digit = digit
                
            # Early exit optimization: 9 is the highest possible digit
            if max_digit == 9:
                return 9
                
            n = n // 10
            
        return max_digit
