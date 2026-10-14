#my approach
class Solution:
    def isPalindrome(self, n):
        num=n
        reverseNum=0
        while n>0:
            d=n%10
            n=n//10
            reverseNum=reverseNum*10+d
        return num==reverseNum
#optimal approach
class Solution:
    def isPalindrome(self, n):
        # Edge cases: negatives, and numbers ending in 0 (except 0 itself)
        if n < 0 or (n % 10 == 0 and n != 0):
            return False
            
        reverseHalf = 0
        while n > reverseHalf:
            reverseHalf = reverseHalf * 10 + (n % 10)
            n = n // 10
            
        # For even length: n == reverseHalf (e.g., 1221 -> 12 == 12)
        # For odd length: n == reverseHalf // 10 (e.g., 12321 -> 12 == 123 // 10)
        return n == reverseHalf or n == reverseHalf // 10
