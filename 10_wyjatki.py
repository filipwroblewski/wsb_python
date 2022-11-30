# try excerpt

def div(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return 'Nie wolno dzielić przez zero'


# print(div(3, 0))
# print(div(3, 2))

# Użytkownik podaje wartosc z klawiatury (liczba calkowita) do momentu podania liczby calkowitej
# while True:
#     try:
#         num = int(input('Podaj liczbe całkowitą: '))
#         print(f'Podałeś {num}')
#         break
#     except ValueError:
#         print('Podana liczba nie jest liczbą całkowitą')

# ----


def square_area(value):
    return value**2


class ValueToLowException(Exception):
    """Base class for other exceptions"""
    pass


try:
    a = float(input('Podaj liczbę: '))
    if a <= 0:
        raise ValueToLowException
    print(f'Wartosc {a}, pole kwadratu: {square_area(a)}')
except OverflowError as e:
    print(f"Zbyt duża wartość. {e}")
except ValueError:
    print("Można wprowadzić jedynie wartości typu float")
except ValueToLowException:
    print('Wartosc musi byc wieksza od zera')
except Exception as e:
    print(f'Wyjątek: {e}')
