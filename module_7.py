import os
import time

for root, dirs, files in os.walk('test'):
    for file in files:
        filepath = os.path.join('test')
        filetime = os.path.getmtime('test')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(r'/Users/mbikb/OneDrive/Документы/GitHub/121/file_os/test/test.txt')
        parent_dir = os.path.dirname(r'/Users/mbikb/OneDrive/Документы/GitHub/121/file_os/test')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},Родительская директория: {parent_dir}')
