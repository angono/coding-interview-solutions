'''
Rotate a matrix (2D array) 90 degrees clockwise.

'''

def rotate_90_clockwise(matrix):
    # Use list comprehension and zip function to rotate the matrix
    rotated_matrix = [list(row[::-1] for row in zip(*matrix))]
    return rotated_matrix

# Example 1:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_90_clockwise(matrix1))
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Example 2:
matrix2 = [
    [1, 2],
    [3, 4]
]
print(rotate_90_clockwise(matrix2))
# Output: [[3, 1], [4, 2]]

# Example 3:
matrix3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(rotate_90_clockwise(matrix3))
# Output: [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]

# Example 4:
matrix4 = [
    [1]
]
print(rotate_90_clockwise(matrix4))
# Output: [[1]]


# Example 5:
matrix5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(rotate_90_clockwise(matrix5))
# Output: [
#   [21, 16, 11, 6, 1],
#   [22, 17, 12, 7, 2],
#   [23, 18, 13, 8, 3],
#   [24, 19, 14, 9, 4],
#   [25, 20, 15, 10, 5]
# ]

# Example 6:
matrix6 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
print(rotate_90_clockwise(matrix6))
# Output: [
#   [7, 5, 3, 1],
#   [8, 6, 4, 2]
# ]

# Example 7:
matrix7 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]
print(rotate_90_clockwise(matrix7))
# Output: [
#   [13, 10, 7, 4, 1],
#   [14, 11, 8, 5, 2],
#   [15, 12, 9, 6, 3]
# ]


# Example 8:
matrix8 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(rotate_90_clockwise(matrix8))
# Output: [
#   [13, 9, 5, 1],
#   [14, 10, 6, 2],
#   [15, 11, 7, 3],
#   [16, 12, 8, 4]
# ]

# Example 9:
matrix9 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]
print(rotate_90_clockwise(matrix9))
# Output: [
#   [16, 13, 10, 7, 4, 1],
#   [17, 14, 11, 8, 5, 2],
#   [18, 15, 12, 9, 6, 3]
# ]

# Example 10:
matrix10 = [
    [1]
]
print(rotate_90_clockwise(matrix10))
# Output: [[1]]


