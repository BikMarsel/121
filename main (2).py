import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
cntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

def generate_password(lenPw, chars):
    password = []
    if digOn == 'y':
        chars += digits
    if ABCon == 'y':
        chars += uppercase_letters
    if abcOn  == 'y':
        chars += lowercase_letters
    if chOn  == 'y':
        chars += punctuation
    if excOn == 'y':
        for c in 'il1Lo0O':
            chars = chars.replace(c,'')
    for i in range(cntPw):
        password = ''.join(random.choice(chars) for _ in range(lenPw))  
        print(password)
        
generate_password(lenPw, chars)
  
    