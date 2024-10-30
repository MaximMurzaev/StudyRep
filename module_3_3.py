def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 12)
print_params(13)
print_params(*[3, 4, 5])

print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['string', [3, 2 ,1], False]
print_params(*values_list)
values_dict = {'a' : True, 'b' : 666, 'c' : 'apple'}
print_params(**values_dict)
values_list_2 = [111, 'banana']
print_params(*values_list_2, 112233)

