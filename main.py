def square_gauss_get_rank(matrix) -> int:
    # Working for square matrix only
    for row in range(len(matrix)):
        if matrix[row][row] == 0:
            for i in range(row + 1, len(matrix)):
                if matrix[i][row] != 0:
                    matrix[i], matrix[row] = matrix[row], matrix[i]
                    break

        if matrix[row][row] == 0:  # double check to avoid zero division
            continue

        leading_element = matrix[row][row]
        for i in range(len(matrix[0])):  # normalize row by leading element
            matrix[row][i] /= leading_element

        for i in range(row + 1, len(matrix)):
            factor = matrix[i][row]
            for j in range(len(matrix[0])):
                matrix[i][j] -= factor * matrix[row][j]
        print(matrix)

    rank = len(matrix)
    for i in range(len(matrix)):
        if all(element == 0 for element in matrix[i]):
            rank -= 1
    return rank


if __name__ == '__main__':
    matrix = [
        [0, 0, 0],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(square_gauss_get_rank(matrix))
