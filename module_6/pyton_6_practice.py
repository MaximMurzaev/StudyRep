from math import pi
from math import sqrt

class Figure:

    __sides = [0]
    __color = [0, 0, 0]
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self.set_color(*color)
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        is_valid_color = True
        for i in color:
            if not (isinstance(i, int) and 0 <= i <= 255):
                is_valid_color = False
                break
        return is_valid_color

    def set_color(self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        is_valid_sides = True
        if self.sides_count == len(sides):
            for side in sides:
                if not isinstance(side, int):
                    is_valid_sides = False
                    break
        else:
            is_valid_sides = False
        return is_valid_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        else:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)

class Circle(Figure):

    sides_count = 1
    __radius = 0

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        p = 0.5 * (len(self))
        a, b, c = map(float, self.get_sides())
        square = sqrt(p * (p - a) * (p - b) * (p - c))
        return square

class Cube(Figure):

    sides_count = 12

    def __init__(self, color, *sides):
        self.set_color(*color)
        list_sides = [sides[0]] * 12
        self.set_sides(*list_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# #Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(f'площадь круга радиусом: {circle1.get_radius()} = {circle1.get_square()}')

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle1 = Triangle((200, 200, 200), 2, 4, 5)
print(triangle1.get_color())
print(f'площадь треугольника: {triangle1.get_square()}')