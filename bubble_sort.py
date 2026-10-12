def bubble_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 4,3,6,10,44]

    print("До сортировки:", numbers)
    print("После сортировки:", bubble_sort(numbers))