#2
my_dict = {'Александр': 'Саша','Евгений':'Женя','Анастасия':'Настя' }
print(my_dict)
#
my_dict['Александр']='Саня'
print(my_dict)
my_dict['Владимир']='Вова'
print(my_dict)
my_dict.update({'Георгий': 'Гоша',
                'Иннокентий':'Кеша'})
print(my_dict)
#my_dict.pop('Евгений')
#print(my_dict)
a = my_dict.pop('Евгений')
print(a)
print(my_dict)
# 3
my_set = {1,2,3, True, False, True, 'gg','ff','gg', 4}
print(my_set)
my_set.update({'zz', 666})
print(my_set)
my_set.discard(666)
print(my_set)