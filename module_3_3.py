#1.Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# print_params()
# print_params(1, 2, 3)
# print_params(d, 5)
# print_params()
# print_params(b=25)
# print_params(c = [1,2,3])

#2.Распаковка параметров:

values_list = [2, 'хочу спать', False]
values_dict = {'a':3,'b':4.5,'c':'сон'}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [1,'cон']
print_params(*values_list_2, 42)