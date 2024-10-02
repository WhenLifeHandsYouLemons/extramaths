def ref_matrix(matrix: list) -> list:
    """Converts a given matrix into it's row echelon form.

    Args:
        matrix (list): The matrix to convert.

    Returns:
        list: The converted matrix.
    """

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

def organise_matrix(matrix: list) -> list:
    """Organises the matrix to have the left-most non-zero values be at the bottom.

    Args:
        matrix (list): The matrix to organise.

    Returns:
        list: The organised matrix.
    """

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
