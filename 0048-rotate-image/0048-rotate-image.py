class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        d = 0
        
        while d < n - 1:
            for i in range(d, n - d - 1):
                matrix[i][n-d-1], matrix[n-d-1][n-i-1], matrix[n-i-1][d], matrix[d][i] = matrix[d][i], matrix[i][n-d-1], matrix[n-d-1][n-i-1], matrix[n-i-1][d]
            d += 1
