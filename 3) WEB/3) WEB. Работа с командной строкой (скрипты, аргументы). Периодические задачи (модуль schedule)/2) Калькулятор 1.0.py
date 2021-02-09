import datetime

import schedule


i = 1


def job():
    global i
    print(f"Запустился {i} раз")
    i += 1
    print(datetime.datetime.now())


# schedule.every(1).hour.at(":00").do(job)  # каждый час
schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
