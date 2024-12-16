import json
from Project.main import f1, f2, f3

def test_ends_with_python():
    path = "/Users/sonyaryabova/PycharmProjects/pythonProject2/Tests/data_test.json"

    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        l = f3(f2(f1(data)))
        for i in l:
            assert i[-16:] == ' с опытом Python'
