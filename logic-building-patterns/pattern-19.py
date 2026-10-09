class Solution:
    def pattern19(self, n):
        for i in range(n):
            for j in range(n,i,-1):
                print("*",end="")
            for j in range(2*i):
                print(" ",end="")
            for j in range(n,i,-1):
                print("*",end="")
            print()
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            for j in range(2*i,2*n-2):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            print()
