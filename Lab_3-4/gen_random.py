import random
def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

for i in gen_random(15, -100, 100):
    print(i, end=' ')
