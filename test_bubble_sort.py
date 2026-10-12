from bubble_sort import bubble_sort


def test_bubble_sort():
    numbers = [5, 2, 8, 1, 4]

    result = bubble_sort(numbers)

    assert result == [1, 2, 4, 5, 8]


def test_empty_list():
    assert bubble_sort([]) == []