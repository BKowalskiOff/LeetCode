class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        base = x
        reversed = 0
        
        while base > 0:
            reversed = 10*reversed + base%10
            base = base//10
            
        return x == reversed