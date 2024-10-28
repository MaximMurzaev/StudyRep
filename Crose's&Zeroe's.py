def generate_field(field):
    for i in field:
        print(* i)

def check_field(field, win):
    for i in range(0, 2):
        if field[i][0] == field[i][1] == field[i][2] != '*':
            print('Игра окончена. Победили', field[i][0])
            win = True
        elif field[0][i] == field[1][i] == field[2][i] != '*':
            print('Игра окончена. Победили', field[0][i])
            win = True
        elif field[0][0] == field[1][1] == field[2][2] != '*':
            print('Игра окончена. Победили', field[0][0])
            win = True
        elif field[0][2] == field[1][1] == field[2][0] != '*':
            print('Игра окончена. Победили', field[0][2])
            win = True
        if win:
            break
    return win

def input_number(field):
    win = False
    for i in range(1, 10):
        win = check_field(field, win)
        if win:
            break
        if i % 2 != 0:
            message = 'Ход крестиков.'
            sign = 'X'
        else:
            message = 'Ход ноликов.'
            sign = '0'
        str_num = int(input(message + " Введите номер строки ")) - 1
        kol_num = int(input(message + " Введите номер колонки ")) - 1
        if field[str_num][kol_num] != '*':
            print("Это поле уже занято. Вы пропускаете ход!")
        else:
            field[str_num][kol_num] = sign
        generate_field(field)
    if not win:
        print('Игра окончена. Увы ничья!')

print('Приветствую в игре "Крестики Нолики"')
field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
generate_field(field)
print('---------------------------------------------------')
input_number(field)