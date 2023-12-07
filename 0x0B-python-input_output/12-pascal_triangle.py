#!/usr/bin/python3
''' pascal_triangle Module '''


def pascal_triangle(n):
    ''' pascal_triangle Module '''
    if n <= 0:
        return []
    else:
        triangle = []
        for row in range(n):
            # Initialize the first row
            if row == 0:
                triangle.append[1]
            else:
                # Calculate subsequent rows
                current = [1]
                for i in range(1, row):
                    value = triangle[row - 1][i - 1] + triangle[row - 1][i]
                    current.append(value)
                current.append(1)
                triangle.append(current)
        return triangle
