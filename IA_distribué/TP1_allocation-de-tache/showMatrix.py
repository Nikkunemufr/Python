def showMatrix(matrix):
    res = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            res += str(matrix[i][j]) + " "
        res+= "\n"
    return res