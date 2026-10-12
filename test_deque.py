import numpy as np
from deque import deque

def test_add_to_tail():
    d = deque(5)

    d.addToTail(10)
    d.addToTail(20)
    d.addToTail(30)

    assert d.accessByIndex(0) == 10
    assert d.accessByIndex(1) == 20
    assert d.accessByIndex(2) == 30

    print("test_add_to_tail пройден")


def test_add_to_head():
    d = deque(5)

    d.addToTail(10)
    d.addToTail(20)
    d.addToHead(5)

    assert d.accessByIndex(0) == 5
    assert d.accessByIndex(1) == 10
    assert d.accessByIndex(2) == 20

    print("test_add_to_head пройден")


def test_head_and_tail():
    d = deque(5)

    d.addToTail(10)
    d.addToTail(20)
    d.addToHead(5)
    d.addToHead(1)

    assert d.accessByIndex(0) == 1
    assert d.accessByIndex(1) == 5
    assert d.accessByIndex(2) == 10
    assert d.accessByIndex(3) == 20

    print("test_head_and_tail пройден")


def test_overflow():
    d = deque(3)

    d.addToTail(10)
    d.addToTail(20)
    d.addToTail(30)

    try:
        d.addToTail(40)

        # Если программа дошла сюда, значит ошибка не появилась
        assert False

    except OverflowError:
        print("test_overflow пройден")


def test_wrong_index():
    d = deque(5)

    d.addToTail(10)

    try:
        d.accessByIndex(5)

        assert False

    except IndexError:
        print("test_wrong_index пройден")


def test_circle():
    d = deque(5)

    d.addToHead(10)
    d.addToHead(20)
    d.addToHead(30)

    assert d.accessByIndex(0) == 30
    assert d.accessByIndex(1) == 20
    assert d.accessByIndex(2) == 10

    print("test_circle пройден")



test_add_to_tail()
test_add_to_head()
test_head_and_tail()
test_overflow()
test_wrong_index()
test_circle()

print("Все тесты успешно пройдены!")