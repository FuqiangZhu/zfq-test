import queue
import time
import threading

q = queue.Queue()


def producer():
    for i in range(10):
        q.put('生产 %s' % i)
        print('producer', i)
        time.sleep(0.3)
    print('等待骨头被取走')
    q.join()
    print('骨头被取完')


def consumer():
    while q.qsize() > 0:
        print(q.get())
        time.sleep(0.3)
        q.task_done()

producer = threading.Thread(target=producer)
consumer = threading.Thread(target=consumer)
producer.start()
consumer.start()

