def show():
    print('Witaj', end=' ')
    print('Anna')


def iloraz(a, b):
    # return a/b
    return a//b


print(iloraz(2, 3))
print(iloraz(9, 2))

'''
Uzytkownik podaje z klawiatury marke, model, pojemnosc, predkosc maksymalna. 
Zdefiniuj funkcje, ktora pobierze dane od uzytkownika i przypisze do slownika. 

Utworz druga funkcje wyswietlajaca dane w formacie:
Marka i model: ... ...
Pojemnosc: ...
Predkosc maksymalna: ...
'''


def setCar():
    car = {'marka': '', 'model': '', 'pojemnosc': '', 'predkosc maksymalna': ''}
    for key in car.keys():
        car[key] = input(f'Podaj {key}:')

    return car


def showCar(car):
    for key, value in car.items():
        print(f'{key.capitalize()}: {value}')


showCar(setCar())
