class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}'

h1= House('ЖК Матрешки', 22)
h2 = House('Особняк', 4)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

