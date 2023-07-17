class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x  == 1:
            return x
        l = 0
        r = x//2
        while l <= r:
            mid = (l+r)//2
            
            if mid*mid == x:
                return mid
            if mid*mid < x:
                l = mid+1
                continue
            else:
                r = mid-1
                
        return r