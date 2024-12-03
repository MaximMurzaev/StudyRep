first = int(input('Введите первое число '))
second = int(input('Введите второе число '))
third = int(input('Введите третье число '))
num_set = {first, second, third}
if len(num_set) == 1:
    print(3)
elif len(num_set) == 2:
    print(2)
else:
    print(0)
