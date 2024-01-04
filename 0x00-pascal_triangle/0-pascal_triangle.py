def pascal_triangle(n):
    if n <= 0: # check if n is less than or equal to 0. If it is, return an empty list.
        return []

    triangle = [] # initialize a list to store the rows of Pascal's Triangle.
    for i in range(n):
        row = [1]  # First element in each row is always 1
        
        for j in range(1, i):
            # Calculate the binomial coefficient
            coefficient = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(coefficient)
        
        if i > 0:
            row.append(1)  # Last element in each row is always 1
        
        triangle.append(row)
    
    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
