#my approach
class Solution:
    def primeUptoN(self, n):
        count=0
        for i in range(2,n+1):
            flag=1
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    flag=0
                    break
            if flag:
                count+=1
        return count
#optimal approach
class Solution:
    def primeUptoN(self, n):
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return sum(is_prime)
