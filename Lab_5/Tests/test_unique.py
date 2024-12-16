from Project.main import Unique

def test_Unique():
    prev = 0
    l = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    for i in Unique(l):
        assert prev != i
        prev = i
