class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 1:
            return

        initial_len = len(matrix)
        added = 0
        for col in range(len(matrix)):
            print("matrix so far", matrix)
            rotated = [matrix[idx][col] for idx in range(len(matrix) - 1, added-1, -1)]
            matrix.insert(col, rotated)
            added += 1
            print("matrix", matrix)

        while initial_len:
            matrix.pop()
            initial_len -= 1


        return matrix


test_case = [[1,2,3],[4,5,6],[7,8,9]]
exp_result =  [[7,4,1],[8,5,2],[9,6,3]]
res = Solution().rotate(test_case)

