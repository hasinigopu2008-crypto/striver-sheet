class Solution:
    def pattern15(self, n):
        for i in range(n):
            for j in range(n,i,-1):
                print(chr(n-j+65),end="")
            print()
