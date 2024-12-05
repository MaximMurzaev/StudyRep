class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors or self.floors == other.floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors or self.floors == other.floors

    def __ne__(self, other):
        return not self == other

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)