#my approach
import math
class Solution:
    def LCM(self, n1, n2):
        return (n1*n2)//math.gcd(n1,n2)
#optimal approach
import math
class Solution:
    def LCM(self, n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        return (n1 // math.gcd(n1, n2)) * n2
