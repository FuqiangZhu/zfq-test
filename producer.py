import queue
import time
import threading


def product():
    for i in range(10):
        q.put('生产 ', i)
        time.sleep(0.3)
    print('等待骨头被取走')
    # q.join()
    print('骨头被取完')


def consumer():
    while q.qsize() > 0:
        print(q.get())
        time.sleep(0.3)
        q.task_done()

q = queue.Queue()


product = threading.Thread(target=product)
consumer = threading.Thread(target=consumer)
product.start()
consumer.start()

