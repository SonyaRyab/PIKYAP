import time
from contextlib import contextmanager

class cm_timer_1():
    def __init__(self):
        self.begin = None
        self.end = None

    def __enter__(self):
        self.begin = time.time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        print('time: %.1f' % (self.end - self.begin))

@contextmanager
def cm_timer_2():
    begin = time.time()
    try:
        yield begin
    finally:  #всегда
        print('time: %.1f' % (time.time() - begin))

with cm_timer_2(): #оператор
    time.sleep(5.5)
