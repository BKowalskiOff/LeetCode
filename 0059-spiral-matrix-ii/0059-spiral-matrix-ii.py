class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1 for i in range(n)] for j in range(n)]
        i = 1
        x = 0
        y = 0
        depth = 0
        while i < n*n:
            for x1 in range(depth, n-depth):
                res[depth][x1] = i
                i += 1
            
            for y1 in range(depth + 1, n-depth):
                res[y1][n - depth - 1] = i
                i += 1
            
            for x1 in range(n-depth-2, depth-1,-1):
                res[n - depth - 1][x1] = i
                i += 1
            
            for y1 in range(n-depth-2, depth,-1):
                res[y1][depth] = i
                i += 1
            depth += 1

        if n%2 == 1:
            res[n//2][n//2] = i

        return res