class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        strings = ['' for i in range(numRows)]
        
        for i, c in enumerate(s):
            row = abs(abs((i%(2*numRows-2))-(numRows-1))-(numRows-1))
            strings[row] += c
                
        return ''.join(strings)