class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            print(mid // len(matrix))
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
                return True
            
            if target > matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                left = mid + 1
            else:
                right = mid -1


        return False