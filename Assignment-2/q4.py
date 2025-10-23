# Program to perform matrix operations using nested lists

# Function to input a 2x2 matrix from the user
def input_matrix(name):
    print(f"Enter elements for {name} (2x2 matrix):")
    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            value = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


# Function to display a matrix neatly
def display_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print("  ".join(f"{val:5}" for val in row))


# Function to compute matrix sum
def matrix_sum(A, B):
    result = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


# Function to compute matrix product
def matrix_product(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result


# Function to sort rows based on their sum
def sort_matrix_by_row_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


# ---------------- Main Program ----------------

# Step 1: Input two 2x2 matrices
A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

# Step 2: Compute sum and product
sum_matrix = matrix_sum(A, B)
product_matrix = matrix_product(A, B)

# Step 3: Sort the product matrix rows by their row sum
sorted_matrix = sort_matrix_by_row_sum(product_matrix)

# Step 4: Display all results
display_matrix(A, "Matrix A")
display_matrix(B, "Matrix B")
display_matrix(sum_matrix, "Sum (A + B)")
display_matrix(product_matrix, "Product (A × B)")
display_matrix(sorted_matrix, "Product Matrix (Rows Sorted by Row Sum)")
