import os.path

class Product:
    def __init__(self, name : str , weight : float, category : str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'

class Shop:

    __file_name = '../products.txt'

    def get_products(self):
        if not os.path.exists(self.__file_name):
            file = open(self.__file_name, 'w+')
            file.close()
            return ''
        file = open(self.__file_name, 'r')
        product_list = file.read()
        file.close()
        return  product_list

    def add(self, *products : Product):
        product_list = self.get_products()
        file = open(self.__file_name, 'w')
        for i in products:
            if product_list.find(i.name) < 0:
                product_list += i.__str__() + '\n'
            else:
                print(f'Продукт {i.name} уже есть в магазине' )
        file.write(product_list)
        file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
