import pytest
import json
from pytest_bdd import scenarios, given, when, then
from Project.main import f1, f2, f3

scenarios("../features/f3.feature")


@pytest.fixture
def applied_functions():
    return {"f1f2": []}


@pytest.fixture
def f3_answer():
    return {"answer": []}


@given("I have loaded json data and used f1 and f2 functions consecutively")
def sorted_list(applied_functions):
    with open("/Users/sonyaryabova/PycharmProjects/pythonProject2/Tests/data_test.json", encoding='utf-8') as file:
        data = json.load(file)
        applied_functions["f1f2"] = f2(f1(data))


@when("the f3 function is used")
def callf1(applied_functions, f3_answer):
    f3_answer["answer"] = f3(applied_functions["f1f2"])


@then("the result should have all elements ending with a certain string")
def result_sorted(f3_answer):
    for i in f3_answer["answer"]:
        assert i[-16:] == ' с опытом Python'
