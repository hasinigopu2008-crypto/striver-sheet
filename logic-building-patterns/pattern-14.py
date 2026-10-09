class Solution:
    def pattern14(self, n):
        for i in range(n):
            for j in range(65,66+i):
                print(chr(j),end="")
            print()
