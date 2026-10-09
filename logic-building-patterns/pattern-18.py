class Solution:
    def pattern18(self, n):
        for i in range(n):
            k=n-i+64
            for j in range(i+1):
                print(chr(k),end=" ")
                k+=1
            print()
