def square_matrix_simple(matrix):
    
  
    res = []
    for row in matrix:
        new_row = [num**2 for num in row]
        res.append(new_row)
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = square_matrix_simple(matrix)

print(new_matrix)   
print(matrix)
