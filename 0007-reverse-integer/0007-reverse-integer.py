class Solution:
    def reverse(self, x: int) -> int:
        lim = 214748364
        sign = 1
        if x < 0:
            x = -1*x
            sign = -1
        res = 0
        while x > 0:
            if res > lim:
                return 0
            res = 10*res + x%10
            x = (x-x%10)//10
        
        return res * sign