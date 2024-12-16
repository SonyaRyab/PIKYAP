import json
from Project.main import f1

def test_sorted():
    path = "/Users/sonyaryabova/PycharmProjects/pythonProject2/Tests/data_test.json"

    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        l = f1(data)
        assert l == sorted(l)
