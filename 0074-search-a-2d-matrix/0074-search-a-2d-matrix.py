class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # basically binary search on steroids
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1

        while l < r:
            mid = (l+r)//2
            y = mid//n
            x = mid%n
            if matrix[y][x] == target:
                return True
            if matrix[y][x] > target:
                r = mid - 1
            else:
                l = mid + 1

        mid = (l+r)//2
        y = mid//n
        x = mid%n

        return True if matrix[y][x] == target else False