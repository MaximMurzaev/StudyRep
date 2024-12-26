def isprime(sum_tree):
    def wrapper(a, b, c):
        result = sum_tree(a, b, c)
        if result > 1:
            is_prime = 'Простое'
            for i in range(2, result):
                if result % i == 0:
                    is_prime = 'Составное'
            print(is_prime)
        else:
            print('Ни простое и ни составное')
        return result
    return wrapper


@isprime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)

print(result)