#декоратор print_result

def print_result(func):
    def inner1(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__) #атрибут функции
        if type(result) == list: #функция вернула список
            for i in result:
                print(i)
        elif type(result) == dict: #функция вернула словарь
            for key, val in zip(result.keys(), result.values()):
                print(key, '=', val)
        else:
            print(result)
    return inner1

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
