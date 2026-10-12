from massiv import Array


def test_set_and_get():
    array = Array(3)

    array.set(0, 10)
    array.set(1, 20)

    assert array.get(0) == 10
    assert array.get(1) == 20


def test_size():
    array = Array(3)

    assert array.show() == [None, None, None]