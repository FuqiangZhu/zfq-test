
import multiprocessing
import time
import os

print('---==---=', os.getppid())


def run():
    time.sleep(2)
    print('---==---', process.pid, os.getppid())

process = multiprocessing.Process(target=run,)
process.start()
