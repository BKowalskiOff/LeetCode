class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = ['' for i in range(numRows)]
        
        row = 0
        up = False
        for i, c in enumerate(s):
            strings[row] += c
            if up:
                if row == numRows-1:
                    up = False
                    row = max(row-1, 0)
                else:
                    row = min(row + 1, numRows - 1)
            else:
                if row == 0:
                    up = True
                    row = min(row + 1, numRows - 1)
                else:
                    row = max(row-1, 0)
                
        return ''.join(strings)