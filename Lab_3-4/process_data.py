import json
import time
import sys
import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

def print_result(func):
    def inner1(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if type(result) == list:
            for i in result:
                print(i)
        elif type(result) == dict:
            for key, val in zip(result.keys(), result.values()):
                print(key, '=', val)
        else:
            print(result)
        return result
    return inner1

class cm_timer_1():
    def __init__(self):
        self.begin = None
        self.end = None

    def __enter__(self):
        self.begin = time.time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        print('time: %.3f' % (self.end - self.begin))  #% - str

def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {}
            for arg in args:
                value = item.get(arg)
                if value is not None:
                    result[arg] = value
            if result:
                yield result

class Unique(object):
    def __init__(self, items, **kwargs):
        self.it = iter(items)
        self.cur = next(self.it)
        self.prev = ''
        if len(kwargs) > 0:
            self.cs = kwargs['ignore_case']
        else:
            self.cs = False

    def __next__(self):
        if type(self.cur) == str and self.cs:
            while self.cur.lower() == self.prev.lower():
                self.cur = next(self.it)
            self.prev = self.cur
            return self.cur
        else:
            while self.cur == self.prev:
                self.cur = next(self.it)
            self.prev = self.cur
            return self.cur

    def __iter__(self):
        return self

path = '/Users/sonyaryabova/PycharmProjects/pythonProject24/Lab_3-4/data_light.json'

with open(path, encoding='utf-8') as file:
    data = json.load(file)

#отсортированный список без повторений
@print_result
def f1(data):
    return list(Unique(sorted(list((field(data, 'job-name')))), ignore_case=False))

#фильтр массива, возвращение слов начинающиеся с программист
@print_result
def f2(seq):
    return list(filter(lambda st: len(st) >= 11 and st[:11].lower() == 'программист', seq))


#добавление строки
@print_result
def f3(seq):
    return list(map(lambda x: x + ' с опытом Python', seq))

#генерация зарплаты
@print_result
def f4(seq):
    return [x + ' ' + str(y) for x, y in zip(seq, list(gen_random(len(seq), 100000, 200000)))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
