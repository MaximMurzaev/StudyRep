

# Посмотреть каталоги из pythonpath
# import sys
# for path in sys.path:
#     print(path)

#импорт внутри функции
# def func():
#     from random import randint
#     randint(1, 10)

#импорт модуля из определенной папки
# def from_folder():
#     import text_files.test

#определение функции внутри самой функции
# def inside_func():
#     a = 1
#     b = 2
#     def func_inside(c, d):
#         print(a * b)
#     func_inside(a, b)
# inside_func()

#анонимная функция
# res = lambda a, b: a * b
# print(res(1, 3))

#посмотреть как работает компилятор
# from dis import dis
# def compile_func():
#     t = 'Как работает компилятор?'
#     print(t)
# compile_func()
# dis(compile_func)

#чтобы создать пакет нужно в папке с подулями создать файл с именем --init__. Код из пакета при импорте выполняется
# точно так же как и при импорте модуля

#Объявление глобальная переменна
# arg = True
# def func():
#     global arg

#Пространство имен идет изнутри наружу. т.е. если имя не найдено внутри функции, то берется из внешней функции
#далее из тела программы, далее из импортируемых. Далее из встроенных. Можео переопределить даже встроенные функции.
#объявить переменную глобальной Global в функции, во встроенной функции nonlocal