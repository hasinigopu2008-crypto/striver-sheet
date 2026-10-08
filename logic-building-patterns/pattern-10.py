class Solution:
    def pattern10(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(n):
            for j in range(n-1,i,-1):
                print("*",end="")
            print()
