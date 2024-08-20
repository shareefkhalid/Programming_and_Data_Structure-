def square_matrix_simple(matrix):
    
  
    result = []
    for row in matrix:
        new_row = [num**2 for num in row]
        result.append(new_row)
    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = square_matrix_simple(matrix)

print(new_matrix)   
print(matrix)
