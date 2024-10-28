num = int(input('Введите число от 3-х до 10-ти '))
result = []
for i in range(1, num):
    next_i = i + 1
    for j in range(next_i, num):
        if num % (i + j) == 0:
            result.append(str(i) + str(j))

print(f'Для числа {num} =', *result)
