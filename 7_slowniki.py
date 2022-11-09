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

print('----- Totolotek -----')
all_nums = list(range(1, 50))  # liczy od 1 do 49
chosen_nums = []
for i in range(6):
    num = int(input(f'Podaj liczbe ({i}/6): '))
    if i in chosen_nums:
        print(f'Ta liczba znajduje sie juz w Twoich numerach!\n{chosen_nums}')
        i -= 1
    else:
        chosen_nums.append(num)

print('= --- =')
winning_num = random.choice(all_nums)
print(f'Wygraywajacy nr to: {winning_num}')
print('= --- =')

if winning_num in chosen_nums:
    print('Brawo! Wygrałeś!')
else:
    print(f'Nie udalo sie. Spróbuj ponownie!')
print(f'Twoje numery to: {chosen_nums}')
