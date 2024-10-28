def count_calls():
    global calls
    calls = calls + 1

def string_info(strg):
    count_calls()
    tuple_string = tuple([len(strg), strg.upper(), strg.lower()])
    return tuple_string

def is_contains(strg, string_list):
    contain = False
    for i in string_list:
        if strg.upper() == i.upper():
            contain = True
            break
    count_calls()
    return contain

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)