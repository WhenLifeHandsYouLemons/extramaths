def ref_matrix(matrix: list) -> list:
    """Converts a given matrix into it's row echelon form.

    Args:
        matrix (list): The matrix to convert. Each item of the list should be a column of the matrix.

    Returns:
        list: The converted matrix. Each item of the list is a column of the matrix.

    Raises:
        TypeError: If the matrix is not a list, or the matrix is not a 2D list.
        ValueError: If all rows of the matrix do not have the same length, or the matrix is empty.
    """

    if type(matrix) is not list:
        raise TypeError("Matrix must be a list.")
    elif type(matrix[0]) is not list:
        raise TypeError("Matrix must be a 2D list.")
    elif len(matrix) == 0:
        raise ValueError("Matrix must not be empty.")
    else:
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError("All rows of the matrix must have the same length.")

    reduced_matrix = matrix

    # Sort matrix by first non-zero value from the left top-to-bottom
    for i in range(len(reduced_matrix)):
        reduced_matrix = organise_matrix(reduced_matrix)

    # Go through each row of the matrix
    row_no = 0
    while row_no < len(reduced_matrix):
        row_val = reduced_matrix[row_no]

        # Find the first non-zero value (pivot column)
        i = 0
        for col_no, col_val in enumerate(row_val):
            # Find the first non-zero value
            if col_val != 0:
                break
            i += 1

        # Make the rest of the column 0
        if i < len(row_val):

            ii = row_no
            while ii < len(reduced_matrix):
                row_val2 = reduced_matrix[ii]

                factor = (row_val2[i] / reduced_matrix[row_no][i])

                if ii != row_no:
                    temp_array = []
                    for j in range(len(row_val2)):
                        try:
                            temp_array.append(round(row_val2[j] - factor * reduced_matrix[row_no][j], 2))
                        except ZeroDivisionError:
                            temp_array.append(row_val2[i])
                    reduced_matrix[ii] = temp_array

                ii += 1

        row_no += 1

    return reduced_matrix

# TODO
def rref_matrix(matrix: list) -> list:
    reduced_matrix = ref_matrix(matrix)

    return reduced_matrix

def organise_matrix(matrix: list) -> list:
    """Organises the matrix to have the left-most non-zero values be at the top.

    Args:
        matrix (list): The matrix to organise. Each item of the list should be a column of the matrix.

    Returns:
        list: The organised matrix.

    Raises:
        TypeError: If the matrix is not a list, or the matrix is not a 2D list.
        ValueError: If all rows of the matrix do not have the same length, or the matrix is empty.
    """

    if type(matrix) is not list:
        raise TypeError("Matrix must be a list.")
    elif type(matrix[0]) is not list:
        raise TypeError("Matrix must be a 2D list.")
    elif len(matrix) == 0:
        raise ValueError("Matrix must not be empty.")
    else:
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError("All rows of the matrix must have the same length.")

    # Go through all rows of the matrix
    row_no = 0
    while row_no < len(matrix) - 1:
        row_val = matrix[row_no]

        cur_count = 0
        for i in row_val:
            if i == 0:
                cur_count += 1
            else:
                break

        next_count = 0
        for i in matrix[row_no + 1]:
            if i == 0:
                next_count += 1
            else:
                break

        if cur_count > next_count:
            matrix[row_no], matrix[row_no + 1] = matrix[row_no + 1], matrix[row_no]

        row_no += 1

    return matrix

def matrix_vector_multiply(matrix: list, vector: list) -> list:
    """Multiplies a matrix by a vector.

    Args:
        matrix (list): The matrix to multiply. Each item of the list should be a column of the matrix.
        vector (list): The vector to multiply. Each item of the list should be a row of the vector.

    Returns:
        list: The resulting vector.

    Raises:
        TypeError: If the matrix is not a list, the vector is not a list, the matrix is not a 2D list, or the vector is not a 1D list.
        ValueError: If the matrix is empty, the vector is empty, or the matrix and vector do not have the same length.
    """

    if type(matrix) is not list:
        raise TypeError("Matrix must be a list.")
    elif type(vector) is not list:
        raise TypeError("Vector must be a list.")
    elif type(matrix[0]) is not list:
        raise TypeError("Matrix must be a 2D list.")
    elif type(vector[0]) is list:
        raise TypeError("Vector must be a 1D list. (Use the vector_multiply function for matrix-matrix multiplication.)")
    elif len(matrix) == 0:
        raise ValueError("Matrix must not be empty.")
    elif len(vector) == 0:
        raise ValueError("Vector must not be empty.")
    elif len(matrix[0]) != len(vector):
        raise ValueError("Matrix and vector must have the same length.")

    result = []

    for row in matrix:
        sum = 0
        for i in range(len(row)):
            sum += row[i] * vector[i]
        result.append(sum)

    return result

def matrix_multiply(matrix1: list, matrix2: list) -> list:
    """Multiplies two matrices.

    Args:
        matrix1 (list): The first matrix to multiply. Each item of the list should be a column of the matrix.
        matrix2 (list): The second matrix to multiply. Each item of the list should be a column of the matrix.

    Returns:
        list: The resulting matrix.

    Raises:
        TypeError: If `matrix1` is not a list, `matrix2` is not a list, `matrix1` is not a 2D list, or `matrix2` is not a 2D list.
        ValueError: If `matrix1` is empty, `matrix2` is empty, `matrix1` and `matrix2` do not have the same number of columns as rows, or `matrix2` is empty.
    """

    if type(matrix1) is not list:
        raise TypeError("Matrix 1 must be a list.")
    elif type(matrix2) is not list:
        raise TypeError("Matrix 2 must be a list.")
    elif len(matrix1) == 0:
        raise ValueError("Matrix 1 must not be empty.")
    elif len(matrix2) == 0:
        raise ValueError("Matrix 2 must not be empty.")
    elif len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrix 1 must have the same number of columns as rows in matrix 2.")
    elif type(matrix1[0]) is not list:
        raise TypeError("Matrix 1 must be a 2D list.")
    elif type(matrix2[0]) is not list:
        raise TypeError("Matrix 2 must be a 2D list.")

    result = []

    for row in matrix1:
        temp_array = []
        for i in range(len(matrix2[0])):
            sum = 0
            for j in range(len(row)):
                sum += row[j] * matrix2[j][i]
            temp_array.append(sum)
        result.append(temp_array)

    return result
