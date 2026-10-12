from quick_sort import quick_sort


def test_quick_sort():
    numbers = [5, 2, 8, 1, 4]

    result = quick_sort(numbers)

    assert result == [1, 2, 4, 5, 8]


def test_empty_list():
    assert quick_sort([]) == []