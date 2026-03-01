class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        r, c = len(matrix), len(matrix[0])
        low, high = 0, r * c - 1

        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // c][mid % c]

            if val==target:
                return True:
            
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False