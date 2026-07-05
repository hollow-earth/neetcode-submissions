class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        idx = 0
        for i in range(len(matrix) // 2):
            idx = len(matrix)-1-i
            _row = matrix[idx]
            matrix[idx] = matrix[i]
            matrix[i] = _row
        for i in range(len(matrix[0])):
            for j in range(i,len(matrix[0])):
                _tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = _tmp
