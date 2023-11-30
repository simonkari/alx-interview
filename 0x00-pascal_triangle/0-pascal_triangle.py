#!/usr/bin/python3
""" Creates a function that returns a lits of lists
of integers representing the Pascal's triangle of n """


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
