def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b - 1)

a = int(input("Введите число, которое будет возведено в степень: "))
b = int(input("Введите число, в степень которого будет возводиться число: "))
print(degree(a, b))
