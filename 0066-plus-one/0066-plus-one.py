class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newDigits = [0] + digits
        
        remainder = 1
        i = len(digits) - 1
        while i >= 0:
            num = digits[i] + remainder
            remainder = num//10
            newDigits[i+1] = num%10
            i -= 1
        
        if remainder > 0:
            newDigits[0] = remainder
            return newDigits
        
        
        return newDigits[1:]