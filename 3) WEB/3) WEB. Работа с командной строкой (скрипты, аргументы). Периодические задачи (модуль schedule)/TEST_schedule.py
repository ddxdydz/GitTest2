import datetime

import schedule
'''
schedule.every(10).minutes.do(job)  # каждые 10 минут
schedule.every().hour.do(job)  # каждый час
schedule.every().day.at("10:30").do(job)  # каждый день в 10-30
schedule.every().monday.do(job)  # каждый понедельник
schedule.every(2).wednesday.at("13:15").do(job)  # Каждую вторую среду в 13-15
schedule.every().minute.at(":17").do(job)  # каждую минуту в 17 секунду

schedule.every(1).to(3).seconds.do(greet, name='Yandex')  # Запускаем задачу в случайное время время от 1 до 3 секунд
'''

'''
mkdir C:/Users/User/Desktop/test_dir/tmp/.tasks/bash/one/
dir /tmp/



mkdir C:\Users\User\Desktop\test_dir\tmp\.tasks\bash\one\
dir C:\Users\User\Desktop\test_dir\tmp
move C:\Users\User\Desktop\test_dir\tmp\.tasks\bash\one C:\Users\User\Desktop\test_dir\tmp\.tasks\one
RD C:\Users\User\Desktop\test_dir\tmp\.tasks\bash

cd C:\Users\User\Desktop\
dir /a:h /w
'''
i = 1


def greet(name):
    global i
    print('Hello', name)
    i += 1
    if i == 5:
        return schedule.CancelJob  # Отменяем задачу после 5 запуска


def job():
    global i
    print(f"Запустился {i} раз")
    i += 1
    print(datetime.datetime.now())


schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()


