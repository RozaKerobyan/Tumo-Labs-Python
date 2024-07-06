def generate_pascals_triangle(num_rows):
    if num_rows <= 0:
        return []

    triangle = [[1]]
    
    for i in range(1, num_rows):
        row = [1]
        prev_row = triangle[i - 1]
        
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)
        triangle.append(row)
    
    return triangle

# Test
num_rows = 10
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)