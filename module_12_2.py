def introspection_info(obj):
    obj_info = {}
    obj_info['type'] = type(obj).__name__
    obj_info['methods'] = dir(obj)
    return obj_info

class MyClass:
    def my_class_function_1(self):
        pass
    def my_class_function_2(self):
        pass

my_class_object = MyClass()

number_info = introspection_info(42)
print(number_info)

my_class_info = introspection_info(my_class_object)
print(my_class_info)