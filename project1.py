print('Hello world!')
print(8)
x=10.1234
print(x)
print("{:.2f}".format(x)) # wyswietlenie z odpowiednim formatem

x=10.1284
print(x)
print("{:.2f}".format(x))

# potegowanie
power=2**10
print(power)

'''
pobieranie danych
z klawiatury
'''
x=2
y=3
result=x^y # XOR ^ (te same wartosci -> 0; 2 inne wartosci -> 1)
print(result)

# konkatenacja +
name=input()
print('Twoje imie: '+name)

length=len(name)
print(length)
print()
firstLetter=name[0]
print(firstLetter)
print(type(name))
print(type(x))
y=10.5
print(type(y))
print('\nPodaj swoj wiek:', end="")
lastLetter=name[len(name)-1]
print(lastLetter)
lastLetter=name[-1]
print(lastLetter)

# konwersja
x='5'
print(type(x))
x=int(x)
print(type(x))
x=x/2
print(x)
print(type(x))
surname='Kowalski'
print()
print(surname[0]) # K
print(surname[:3]) # Kow
print(surname[6]) # k
print(surname[-2]) # k
print(surname[-2:]) # ki
print(surname[:-2]) # Kowals
print(surname[:-2:2]) # Kwl (od 1st do ostatnich 2, z przeskokiem co 2 znaki)
