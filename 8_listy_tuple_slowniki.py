# listy
progr = ['PHP', 'Python']
print(progr)
progr.append('C#')
cont = progr.count('Python')
print(f'Python wystepuje {cont} razy')

# tuple
str_tuple = ('Janusz', 'Anna')
int_tuple = (1, 2, 3)

print(int_tuple)

test = (1)
print(type(test))

test1 = (1,)
print(type(test1))

first = int_tuple[0]
print(first)

# int_tuple.append(int_tuple) # AttributeError: 'tuple' object has no attribute 'append'
# tuple nie mozna modyfikowac

# wyszukiwanie
if 2 in int_tuple:
    print('W tuple int_tuple istnieje 2')
else:
    print('W tuple int_tuple nie istnieje 2')

# slowniki
person = {
    'name': 'Anna',
    'surname': 'Nowak'
}

print(person)
print(type(person))
print(person['name'])
print(person.keys())
# w przypadku braku klucza wyswietla 2nd parametr
print(person.get('height', 'brak danych'))
print(person.get('name', 'brak danych'))

person['height'] = 180
print(person.get('height', 'brak danych'))

'''
Utworz slownik i przypisz mu 3 imiona podane z klawiatury
klucze w slowniku to liczby calkowite 0, 1, 2
wyswietl te dane w formacie:
Imię1: ...
Imię2: ...
Imię3: ...
'''
names = {}
for i in range(3):
    names[i] = input(f'Podaj imie (nr {i+1}): ')

for key, value in names.items():
    print(f'Imię{key+1}: {value}')
