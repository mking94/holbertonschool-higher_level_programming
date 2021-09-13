def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j == (len(matrix[i]) - 1):
                print(matrix[i][j], end="$\n")
            else:
                print(matrix[i][j], "", end="")
