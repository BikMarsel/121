calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
string = "Capybara"
print(string_info(string))
string_info(string)

def is_contains(string, list_to_search):
    count_calls()
    if (string.upper() == list_to_search[0] or string.upper() == list_to_search[1] or string.upper() == list_to_search[2]):
        print('False')
    else:
        print('True')
    return string.upper(), list_to_search
string = 'Urban'
list_to_search = ['ban', 'BaNaN', 'urBAN']

#
string_info('У лукоморья дуб')
is_contains('Зеленый', ['златая','Цепь', 'На дубе том'])
print(calls)

