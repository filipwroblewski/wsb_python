import random as r
import math as m

# import math as m
print(m.pow(2, 5))

# import random as r
rand = r.random()
print(rand)

randOfList = r.choice([1, 2, 3, 4])
print(randOfList)

print(r.randrange(10, 20))
print(r.randrange(5))
print(r.randrange(9, 13, 2))

print('----------------')

numList = [10, 20, 30, 40, 45]
numTuple = (1, 2, 3, 4, 5)
text = 'Janusz'

print(f'Lista: {r.choice(numList)}')
print(f'Tuple: {r.choice(numTuple)}')
print(f'Text: {r.choice(text)}')

print('----------------')

print(numList)
r.shuffle(numList)
print(numList)
