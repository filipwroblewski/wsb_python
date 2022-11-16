import random
slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}
print(slownik)
print(slownik['klucz1'])

'''
utowrz slownik o nazwie worker
zawierajacy klucz:
    imie
    nazwisko
    miasto
    wiek
    imiona_dzieci
    imiona_rodzicow
'''
worker = {
    'imie': 'Bob',
    'nazwisko': 'Bobson',
    'miasto': 'CityName',
    'wiek': 46,
    'imiona_dzieci': ['DoughterName', 'SonName'],
    'imiona_rodzicow': ['MotherName', 'FatherName']
}

print(worker)
print(worker['imiona_dzieci'])
print(worker['imiona_dzieci'][0])

worker['height'] = 180
print(worker)

key = 'imie'

if key in worker:
    del worker[key]
    print(f'klucz {key} zostal usuniety!')
else:
    print(f'klucz {key} nie zostal usuniety!')
print(worker)

# dokonczyc slowniki

'''
utworz program totolotek
uzytkownik podaje 6 liczb
'''

print('\n\n----- Totolotek -----')
all_nums = list(range(1, 50))  # liczby od 1 do 49
chosen_nums = []
while len(chosen_nums) < 6:
    num = int(input(f'Podaj liczbe ({len(chosen_nums)+1}/6): '))
    if num in chosen_nums:
        print(f'Ta liczba znajduje sie juz w Twoich numerach!\n{chosen_nums}')
    else:
        chosen_nums.append(num)

print('= --- =')
winning_num = random.choice(all_nums)
print(f'Wygraywajacy nr to: {winning_num}')
print('= --- =')
print(f'Twoje numery to: {chosen_nums}')

if winning_num in chosen_nums:
    print('Brawo! Wygrałeś!')
else:
    print(f'Nie udało Ci się wygrać.')
