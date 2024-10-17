from math import trunc

my_dict ={'my_name':'Maksim', 'my_age':40, 'im_tdudy': True}
print(my_dict)
print(my_dict['my_name'])
print(my_dict.get('my_year'))
my_dict.update({'my_year':1984, 'i_live':'in city'})
print(my_dict)
print(my_dict.pop('my_age'))
print(my_dict)

my_set = {1,2,3,3,2,1,'maksim',True,'tea',True}
print(my_set)
my_set.add(4)
my_set.add('coffee')
print(my_set)
my_set.remove(2)
print(my_set)