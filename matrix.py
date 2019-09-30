"""
Nathan, Ryan, Jon
Liberty University
Python team ACM Competition
"""


def check_if_cols_equal(matrix):
    is_equal = True
    row_length = len(matrix)
    col_length = len(matrix[0])

    sum_of_col = 0

    prev_sum = -1
    for r in range(row_length):
        for c in range(col_length):
            sum_of_col += matrix[r][c]
        if prev_sum >= 0 and sum_of_col != prev_sum:
            is_equal = False
        prev_sum = sum_of_col
        sum_of_col = 0

    return(is_equal)


def check_if_rows_equal(matrix):
    is_equal = True
    row_length = len(matrix)
    col_length = len(matrix[0])

    sum_of_row = 0

    prev_sum = -1
    for c in range(col_length):
        for r in range(row_length):
            sum_of_row += matrix[r][c]
        if prev_sum >= 0 and sum_of_row != prev_sum:
            is_equal = False
        prev_sum = sum_of_row
        sum_of_row = 0

    return(is_equal)


def matrix_num_of_steps(matrix, num_of_steps=0):
    col_equal = check_if_cols_equal(matrix)
    row_equal = check_if_rows_equal(matrix)

    if col_equal and row_equal:
        # Done: return the final number of steps
        return num_of_steps
    # Otherwise keep changing stuff
    else:
        if col_equal and not row_equal:
            row = first_difference(matrix, 'rows')
        elif not col_equal and row_equal:
            col = first_difference(matrix, 'rows')
        else:
          

            else:

        return(matrix, num_of_steps + 1)


def highest_frequency(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])

    sums_of_rows = []
    for c in range(col_length):
        sum_of_row = 0
        for r in range(row_length):
            sum_of_row += matrix[r][c]
        sums_of_rows.append(sum_of_row)
    highest_row = max(set(sums_of_rows), key=sums_of_rows.count)

    sums_of_cols = []
    for r in range(row_length):
        sum_of_col = 0
        for c in range(col_length):
            sum_of_col += matrix[r][c]
        sums_of_cols.append(sum_of_col)
    highest_col = max(set(sums_of_cols), key=sums_of_cols.count)

    return(highest_row, highest_col)


def first_difference(matrix, rows=True):
    return None













matrix = []

with open('matrix_input.txt') as matrix_input:
    num_of_cases = int(matrix_input.readline())
    for _ in range(num_of_cases):
        next_line = matrix_input.readline()
        num_of_rows = int(next_line.split(" ")[0])
        num_of_columns = int(next_line.split(" ")[1])
        for _ in range(num_of_rows):
            inner_matrix = []
            column = matrix_input.readline()
            for c in range(num_of_columns):
                inner_matrix.append(int(column[c]))
            matrix.append(inner_matrix)
        print(matrix)  # Place to put function call to process case
        matrix = []

"""
Matrix Format:

[[1, 1, 1], [1, 1, 1]]
[[0, 1, 1], [0, 1, 1], [0, 1, 1]]
[[0, 0, 1], [0, 0, 0]]
"""
