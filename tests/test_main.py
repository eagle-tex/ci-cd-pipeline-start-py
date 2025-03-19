from src.main import add, subtract


def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 7) == 12


def test_subtract_function():
    assert subtract(5, 3) == 2
    assert subtract(1, 2) == -1
    assert subtract(17, 8) == 9
