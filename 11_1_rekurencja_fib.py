def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    else:
        return podstawa * potega(podstawa, wykladnik - 1)


# print(potega(3, 3))
# print(potega(3, 2))
# print(potega(3, 1))
# print(potega(3, 0))

class FibValueError(Exception):
    """Base class for other exceptions"""
    pass


def fib(n):
    if n <= 0:
        raise FibValueError
        print(
            f'Ciąg Fibboniaciego może być wyliczony dla wartości n > 0. Podałeś n = {n}')
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-2)+fib(n-1))


print(fib(6))
