def read_sparse_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rows = int(lines[0].split('=')[1])
        cols = int(lines[1].split('=')[1])
        data = {}
        for line in lines[2:]:
            row, col, value = map(int, line.strip()[1:-1].split(','))
            if row not in data:
                data[row] = {}
            data[row][col] = value
    return rows, cols, data

def get_element(matrix, row, col):
    data = matrix[2]
    return data.get(row, {}).get(col, 0)

def set_element(matrix, row, col, value):
    data = matrix[2]
    if row not in data:
        data[row] = {}
    data[row][col] = value

def add_matrices(matrix1, matrix2):
    if matrix1[0] != matrix2[0] or matrix1[1] != matrix2[1]:
        raise ValueError("Matrices must have the same dimensions for addition")
    
    result = (matrix1[0], matrix1[1], {})
    for row in range(matrix1[0]):
        for col in range(matrix1[1]):
            value = get_element(matrix1, row, col) + get_element(matrix2, row, col)
            if value != 0:
                set_element(result, row, col, value)
    return result

def subtract_matrices(matrix1, matrix2):
    if matrix1[0] != matrix2[0] or matrix1[1] != matrix2[1]:
        raise ValueError("Matrices must have the same dimensions for subtraction")
    
    result = (matrix1[0], matrix1[1], {})
    for row in range(matrix1[0]):
        for col in range(matrix1[1]):
            value = get_element(matrix1, row, col) - get_element(matrix2, row, col)
            if value != 0:
                set_element(result, row, col, value)
    return result

def multiply_matrices(matrix1, matrix2):
    if matrix1[0] != matrix2[0] or matrix1[1] != matrix2[1]:
        raise ValueError("Matrices must have the same dimensions for addition")
    
    result = (matrix1[0], matrix1[1], {})
    for row in range(matrix1[0]):
        for col in range(matrix1[1]):
            value = get_element(matrix1, row, col) + get_element(matrix2, row, col)
            if value != 0:
                set_element(result, row, col, value)
    return result

def matrix_to_string(matrix):
    rows, cols, data = matrix
    result = f'rows={rows}\ncols={cols}\n'
    for row in data:
        for col in data[row]:
            result += f'({row}, {col}, {data[row][col]})\n'
    return result

def main():
    operation = input("Enter the operation (add, subtract, multiply): ")
    first_path = input("Enter the path for the first matrix file: ")
    second_path = input("Enter the path for the second matrix file: ")
    
    try:
        matrix1 = read_sparse_matrix(first_path)
        matrix2 = read_sparse_matrix(second_path)

        if operation.lower() == 'add':
            result = add_matrices(matrix1, matrix2)
        elif operation.lower() == 'subtract':
            result = subtract_matrices(matrix1, matrix2)
        elif operation.lower() == 'multiply':
            result = multiply_matrices(matrix1, matrix2)
        else:
            print("Invalid operation")
            return

        print("Result:")
        print(matrix_to_string(result))
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
