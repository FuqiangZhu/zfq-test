
import threading
import time

num = 0

lock = threading.BoundedSemaphore(1)


def run():
    time.sleep(0.5)
    lock.acquire()
    global num
    num += 1
    print(num)
    lock.release()

res = []
for i in range(100):
    r = threading.Thread(target=run)
    r.start()
    res.append(r)

for r in res:
    r.join()

print(num)
