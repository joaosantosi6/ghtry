from sample import add

def test_example():
    assert 1 + 1 == 2

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 1