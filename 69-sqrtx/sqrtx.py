class Solution:
    def mySqrt(self, x: int) -> int:
        for n in range(0,x//2 +2):
            if n * n == x :
                return n
            elif n*n > x:
                return n-1 
        