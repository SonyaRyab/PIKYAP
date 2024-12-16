import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

# Итератор для удаления дубликатов
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

data = gen_random(10, 1, 3)
data1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for i in Unique(data):
    print(i, end=' ')
for i in Unique(data1, ignore_case=True):
    print(i, end=' ')
