
def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding  = 'utf-8')
    str_num = 0
    for i in strings:
        str_num += 1
        strings_positions[(str_num, file.tell())] = i
        file.write(i + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)