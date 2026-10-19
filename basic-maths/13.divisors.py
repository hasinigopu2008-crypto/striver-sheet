#my approach
class Solution:
    def divisors(self, n):
        lst=[]
        for i in range(1,n+1):
            if n%i==0:
                lst.append(i)
        return lst
#optimal approach
class Solution:
    def divisors(self, n):
        lst = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                lst.append(i)
                if i != n // i:
                    lst.append(n // i)
        return sorted(lst)
