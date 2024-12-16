import pytest
from pytest_bdd import scenarios, given, when, then
from Project.main import Unique

scenarios("../features/unique.feature")
@pytest.fixture
def fixlists():
    return {"list": [], "results": []}

@given("I have a sorted list of integers")
def sorted_list(fixlists):
    fixlists["list"] = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]


@when("Unique iterates over it")
def iterating(fixlists):
    for i in Unique(fixlists["list"]):
        fixlists["results"].append(i)


@then("Iterator returns only unique integers")
def results_unique(fixlists):
    prev = 0
    for i in fixlists["results"]:
        assert prev != i
        prev = i
