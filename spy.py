import datetime


def log(msg):
    file = open('log.txt', 'a', encoding='utf-8')
    file.write(f'Дата: {datetime.datetime.now().time()}\nID пользователя: {msg.from_user.id}\n'
               f'Сообщение пользователя: {msg.text}\n')
    file.close()

