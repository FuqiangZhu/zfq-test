

import threading
import time

event = threading.Event()
# event.wait()


def light():
    count = 0
    event.set()  # 先设置绿灯

    while True:
        if 5 < count < 10:
            event.clear()  # 把标识清空
            print('\033[31;1m 红灯 %d \033[0m' % count)
        elif count > 10:
            event.set()  # 变绿灯
            count = 0
            print('clear %d' % count)
        else:
            print('\033[32;1m 绿灯 %d \033[0m' % count)

        time.sleep(0.3)
        count += 1


def car():
    while True:
        if event.is_set():
            print('绿灯 车走')
        else:
            print('红灯 车停')
        time.sleep(0.3)

light = threading.Thread(target=light)
light.start()

car = threading.Thread(target=car)
car.start()
