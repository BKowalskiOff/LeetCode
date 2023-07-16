class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        x = 1
        y = 2

        i = 3
        while i <= n:
            x, y = y, x + y
            i += 1
        
        return y