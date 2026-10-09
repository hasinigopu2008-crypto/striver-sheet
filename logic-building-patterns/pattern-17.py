class Solution:
    def pattern17(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(i+1):
                print(chr(j+65),end="")
            for j in range(i):
                print(chr(i-j+64),end="")
            print()
