class Solution:
    def pattern13(self, n):
        k=1
        for i in range(n):
            for j in range(i+1):
                print(k,end=" ")
                k+=1
            print()
