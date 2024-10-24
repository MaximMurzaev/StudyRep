def get_matrix(n, m, value):
    matrix = list()
    for i in range(0, n):
        new_list = list()
        matrix.append(new_list)
        for j in range(0, m):
            new_list.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(*[2 , 3, 1])
result3 = get_matrix(*[5, 5, 100])
print(result1)
print(result2)
print(result3)
