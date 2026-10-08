class Solution:
    def pattern12(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end="")
            for j in range(2*i,2*n-2):
                print(" ",end="")
            for j in range(i+1):
                print(i-j+1,end="")
            print()
