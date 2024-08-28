def send_email(message, recipient, sender='university.help@gmail.com'):  # 1 пункт задачи
    # #     #         if recipient == sender:                                              # 3 пункт задачи
    #             print('Нельзя отправить письмо самому себе!')
    #
    # send_email(message='Напоминаю самому себе о вебинаре', recipient='university.help@gmail.com')
    #
    if "@" not in recipient or not recipient.endswith(
            (".com", ".ru", ".net ")) or "@" not in sender or not sender.endswith(
            (".com", ".ru", ".net ")):  # 2 пункт задачи
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)


send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# #
#     print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient) # 4 пункт задачи
# send_email(message='Это сообщение для проверки связи', c='vasyok1337@gmail.com')
#
#     print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient) # 5 пункт задачи
# send_email(message='Вы видите это сообщение как лучший студент курса', recipient='urban.fan@mail.ru', sender='urban.info@gmail.com')


# х = 'заканчивается указанным суффиксом @'
# х.endswith('@')
# print(х)
# х.endswith('иксом')
# print(х)
