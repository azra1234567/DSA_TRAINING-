
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
	"""Return True if target exists in the 2D matrix.

	The matrix is assumed to satisfy the properties listed above.  We
	perform a binary search on the range [0, m*n).
	"""

	if not matrix or not matrix[0]:
		return False

	m, n = len(matrix), len(matrix[0])
	left, right = 0, m * n - 1

	while left <= right:
		mid = (left + right) // 2
		# map 1D index to 2D
		row, col = divmod(mid, n)
		value = matrix[row][col]

		if value == target:
			return True
		elif value < target:
			left = mid + 1
		else:
			right = mid - 1

	return False


if __name__ == "__main__":
	# simple test
	mat = [
		[1, 3, 5, 7],
		[10, 11, 16, 20],
		[23, 30, 34, 50],
	]
	print(search_matrix(mat, 3))   # True
	print(search_matrix(mat, 13))  # False
