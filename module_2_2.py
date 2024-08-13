first = int(42)
second = int(69)
third = int(42)
if first == second == third:
    print('Ответ по пункту № 1:', 3)
elif first == second or second == third or first == third:
    print('Ответ по пункту № 2:', 2)
elif first != second or second != third or first != third:
    print('Ответ по пункту № 3:', 0)


# first = int(input('Введите первое число:'))
# second = int(input('Введите второе число:'))
# third = int(input('Введите третье число:'))