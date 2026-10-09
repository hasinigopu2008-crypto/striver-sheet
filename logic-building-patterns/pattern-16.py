class Solution:
    def pattern16(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(i+65),end="")
            print()
