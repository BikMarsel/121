

def add_everything_up(a, b):
    """
    add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    TypeError - когда a и b окажутся разными типами (числом и строкой),
    то возвращать строковое представление этих двух данных вместе (в том же порядке).
    Во всех остальных случаях выполнять стандартные действия.
    """
    return str(a) + str(b) if (type(a) == float and type(b) == str) or (type(a) == str and type(b) == int) else float(a) + int(b)

try:
    print(add_everything_up(123.456, 'строка'))
except TypeError as e:
    print(f'Попытка не пытка, как говорил Лаврентий Павлович: {e}')

try:
    print(add_everything_up('яблоко', 4215))
except TypeError as e:
    print(f'Попытка не пытка, как говорил Лаврентий Павлович: {e}')

try:
    print(add_everything_up(123.456, 7))
except TypeError as e:
    print(f'Попытка не пытка, как говорил Лаврентий Павлович: {e}')


