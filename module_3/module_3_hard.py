
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calc_values(value, result = 0):
    if isinstance(value, int):
        result += value
        return result
    elif isinstance(value, str):
        result += len(value)
        return result
    elif isinstance(value, dict):
        for i in value.items():
           result = calc_values(i, result)
        return result
    else:
        for i in value:
            result = calc_values(i, result)
        return result
result = calc_values(data_structure)
print(result)