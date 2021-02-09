import datetime

import schedule


message = input('message: ')
while True:
    diapason = input('diapason(00-07): ')
    try:
        diapason = list(map(
            int, diapason.split('-')))
        assert len(list(filter(
            lambda elem: 0 <= elem <= 12, diapason)))
        assert len(diapason) == 2
        break
    except ValueError as e:
        print(e)
    except AssertionError as e:
        print('AssertionError')


def cu():
    cur_hour = datetime.datetime.now().hour
    if cur_hour - 1 not in range(*diapason):
        print(message * cur_hour)


schedule.every(1).hour.at(":00").do(cu)  # каждый час

while True:
    schedule.run_pending()
