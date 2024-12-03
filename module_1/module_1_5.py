immutable_var = (1, 'gus', [3,2,1], True)
print(immutable_var)
# immutable_var[3] = False
print(immutable_var)
mutable_list = [1, 'gus', [3,2,1], True]
print(mutable_list)
mutable_list.remove(1)
mutable_list[1][1] = 0
print(mutable_list)

