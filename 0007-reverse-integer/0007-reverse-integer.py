class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            x = -1*x
            sign = -1
        res = 0
        while x > 0:
            res = 10*res + x%10
            x = x//10
        
        if res < -2**31 or res > 2**31 - 1:
                return 0
        
        return res * sign