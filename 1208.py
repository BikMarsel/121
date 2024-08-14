grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# средний балл
a = float(sum(grades[0]))/len(grades[0])
b = float(sum(grades[1]))/len(grades[1])
c = float(sum(grades[2]))/len(grades[2])
d = float(sum(grades[3]))/len(grades[3])
e = float(sum(grades[4]))/len(grades[4])
print(a, b, c, d, e)
# перевод в список АВС
f = sorted(list(students))
print(f)
# Первый вариант словаря
s = {f[0]: a, f[1]:b,f[2]:c,f[3]:d, f[4]:e}
print(s)
# Второй вариант словаря
z = dict([[f[0],a], [f[1],b], [f[2],c], [f[3],d], [f[4],e]])
print(z)
# Третий вариант словаря
w = dict(zip([f[0],f[1],f[2],f[3],f[4]],[a,b,c,d,e]))
print(w)
print(type(s))
print(type(z))
