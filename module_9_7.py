def is_prime(func):
    def wrapper(*args, ** kwargs):
        result = func(*args, ** kwargs)
        _sum = sum(args)
        j = 0
        for i in range(2, _sum // 2 + 1):
            if _sum % i == 0:
                j = j + 1
        if j <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper



@is_prime

def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
