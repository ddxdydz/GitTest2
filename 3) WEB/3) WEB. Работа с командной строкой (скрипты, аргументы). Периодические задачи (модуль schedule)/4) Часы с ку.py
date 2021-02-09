import datetime

import schedule


def cu():
    cur_hour = datetime.datetime.now().hour
    print('КУ' * (cur_hour - 12 if cur_hour > 12 else cur_hour))


schedule.every(1).hour.at(":00").do(cu)  # каждый час

while True:
    schedule.run_pending()
