#my approach
class Solution:
    def GCD(self, n1, n2):
        while n2!=0:
            n1,n2=n2,n1%n2
        return n1
#optimal approach
import math
class Solution:
    def GCD(self, n1, n2):
        return math.gcd(n1, n2)
