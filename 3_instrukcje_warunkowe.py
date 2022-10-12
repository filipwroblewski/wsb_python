x=input('Podaj wartość:')
if x=='10':
	print('Podałeś 10')
	print('xzc')
else:
	print('Inna wartość niż 10')
print(type(x))

y=False
if y:
	print('prawda')
else:
	print('fałsz')

print('prawda') if y else print('fałsz')
# value_when_true if condition else value_when_false

'''
Użytkownik podaje wartości trzech zmiennych x,y,z
wyświetl, która z tych 3 wartości jest największa.
Wykorzystaj instrukcje warunkowe
'''
x=input('Podaj x:')
y=input('Podaj y:')
z=input('Podaj z:')
if x>=y and x>=z:
	print(x)
elif y>=z:
	print(y)
else:
	print(z)
