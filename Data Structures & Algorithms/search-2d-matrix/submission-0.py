class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m =  len(matrix[0])
        bottom = 0
        top = (n*m) -1
        row = lambda i :  i // m
        col = lambda i :  i % m
        while bottom <= top:
            middle = bottom + (top-bottom) // 2
            num = matrix[row(middle)][col(middle)]
            if num > target:
                top = middle - 1
            elif num < target:
                bottom = middle+1
            else:
                return True
        return False