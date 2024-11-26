class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
    def go_to(self, new_floor):
        if int(new_floor) > self.floors:
            print(f'Этажа с номером {new_floor} не существует! В доме "{self.name}" их {self.floors}')
        else:
            i = 1
            for i in range(0, new_floor + 1):
                print(i)


h1= House('ЖК Матрешки', 22)
h2 = House('Особняк', 4)

h1.go_to(5)
h2.go_to(5)

