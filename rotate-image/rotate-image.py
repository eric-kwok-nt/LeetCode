from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        arr_side_len = len(matrix)
        num_layers = arr_side_len // 2
        for layer in range(num_layers):
            layer_side_len = arr_side_len - layer * 2
            i = 0
            while layer_side_len - i > 1:
                (
                    matrix[(i + layer)][-layer - 1],
                    matrix[-layer - 1][-(i + layer) - 1],
                    matrix[-(i + layer) - 1][layer],
                    matrix[layer][(i + layer)],
                ) = (
                    matrix[layer][(i + layer)],
                    matrix[(i + layer)][-layer - 1],
                    matrix[-layer - 1][-(i + layer) - 1],
                    matrix[-(i + layer) - 1][layer],
                )
                i += 1


if __name__ == "__main__":
    matrix_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    matrix_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    Sol = Solution()
    Sol.rotate(matrix_2)
    print(matrix_2)
