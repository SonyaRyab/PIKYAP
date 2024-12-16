import pytest
import json
from pytest_bdd import scenarios, given, when, then
from Project.main import f1

scenarios("../features/f1.feature")

@pytest.fixture
def loadJson():
    return {"data": [], "path": "/Users/sonyaryabova/PycharmProjects/pythonProject2/Tests/data_test.json"}

@pytest.fixture
def f1_answer():
    return {"answer": []}

@given("I have loaded json data")
def sorted_list(loadJson):
    with open(loadJson["path"], encoding='utf-8') as file:
        loadJson["data"] = json.load(file)

@when("the f1 function is used")
def callf1(loadJson, f1_answer):
    f1_answer["answer"] = f1(loadJson["data"])

@then("the result should be sorted")
def result_sorted(f1_answer):
    assert f1_answer["answer"] == sorted(f1_answer["answer"])
