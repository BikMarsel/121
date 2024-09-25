a = 3
def test_function(a):
    b = a+2
    def inner_function(a):
        b = a+1
        if b < 5:
            print("Я в области видимости функции test_function()")
        else:
            print('Иди спать')
    inner_function(b)
    return a

# inner_function(3)
test_function(1)






