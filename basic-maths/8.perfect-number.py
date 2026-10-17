#my approach
class Solution:
    def isPerfect(self, n: int) -> bool:
        num=n
        result=0
        for i in range(1,n//2+1):
            if n%i==0:
                result+=i
        return result==num
#optimal approach
class Solution:
    def isPerfect(self, n: int) -> bool:
        if n <= 1:
            return False   
        result = 1 
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                result += i
                if i != n // i:
                    result += n // i        
        return result == n
