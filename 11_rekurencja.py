def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    else:
        return podstawa * potega(podstawa, wykladnik - 1)


print(potega(3, 3))
print(potega(3, 2))
print(potega(3, 1))
print(potega(3, 0))
