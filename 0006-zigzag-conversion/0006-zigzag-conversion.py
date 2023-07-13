class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        strings = ['' for i in range(numRows)]
        row = 0
        up = False
        
        for i, c in enumerate(s):
            if row == 0 or (row == (numRows - 1)):
                up = not up
            strings[row] += c
            
            if up:
                row += 1
            else: 
                row -= 1
            
        return ''.join(strings)