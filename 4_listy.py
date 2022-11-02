from operator import index


programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))
first = programowanie[0]
print('Pierwszy element: ', first)

threeElements = programowanie[:3]
print('Trzy elementy: ', threeElements)

lastElement = programowanie[-1]
print('Ostatni element: ', lastElement)

# dodanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

# zliczanie elementow w liscie
countPython = programowanie.count('Python')
print(countPython)

# zliczanie elementow w liscie
countElements = len(programowanie)
print('Ilosc elementow w liscie: ' + str(countElements))

# polaczenie list
anotherList = ['C', 'C++']
programowanie.extend(anotherList)
# programowanie += anotherList
print('Lista programowanie: ' + str(programowanie))
print('Lista anotherList: ' + str(anotherList))

# usuwanie elementow z listy
new = programowanie
print('New list: ' + str(new))
new.clear()
print('New list (after clear): ' + str(new))

# usuniecie elementow rowniez z tej listy bo nie ma kopii tylko jest przekazanie referencji
print(programowanie)

'''
Dodaj listę o nazwie: country
Przypisz do niej 5 elementów
Poproś użytkownika, aby dodał dwa nowe elementy do listy
Uzytkownikowi wyświetl listę do wyboru:
1) Wyświetl pierwsze 3 elementy listy
2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)
3) Wyświetl zawartość listy
4) Wyczyść zawartość listy
5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)
Użytkownik raz dokonuje wyboru z listy.
Wyświetl zawartość listy po wykonaniu operacji przez użytkownika.
'''

country = ['Polska', 'Włochy', 'Hiszpania', 'Grecja', 'Norwegia']
newName1 = input('Wprowadź nazwę kraju: ')
newName2 = input('Wprowadź nazwę kraju: ')
addedElems = [newName1, newName2]
country.extend(addedElems)

menu = '1) Wyświetl pierwsze 3 elementy listy\n2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)\n3) Wyświetl zawartość listy\n4) Wyczyść zawartość listy\n5) Znajdź element w liście, który poda użytkownik\nq) Zakończenie działania\n\nWybor: '
option = ''
while option != 'q':
    option = input(menu)
    if option == '1':
        print(f'pierwsze 3 elementy listy: {country[:3]}')
    elif option == '2':
        print(f'elementy listy, które dodałem: {addedElems}')
    elif option == '3':
        print(f'Wyświetl zawartość listy: {country}')
    elif option == '4':
        print(f'Wyświetl zawartość listy: {country.clear()}')
    elif option == '5':
        indexOfElem = int(input('Index elementu z listy do sprawdzenia: '))
        if indexOfElem <= len(country):
            print(
                f'Element nr {indexOfElem} jest dodany do listy ({country[indexOfElem]})')
        else:
            print('Nie ma podanego elementu w liście')
    elif option == 'q':
        break
print(f'Wyświetl zawartość listy: {country}')
