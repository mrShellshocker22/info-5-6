def sum_of_row(matrix, row_number: int):
    row = matrix[row_number]
    row = 0
    for item in row:
        # row_sum = row_sum + item
        row_sum += item
    return row_sum

def sum_of_column(matrix, column_number: int):
    column_sum = 0
    for row in matrix:
        column_sum = column_sum + row[column_number]
    return column_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]
#my_sum = sum_of_row(m, 1)
my_sum = sum_of_column(m, 2)
print(my_sum)