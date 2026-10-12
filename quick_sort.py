def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    left = []
    middle = []
    right = []

    for number in numbers:
        if number < pivot:
            left.append(number)
        elif number > pivot:
            right.append(number)
        else:
            middle.append(number)

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 4]

    print("До сортировки:", numbers)
    print("После сортировки:", quick_sort(numbers))