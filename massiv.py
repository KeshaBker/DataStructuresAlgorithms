class Array:
    def __init__(self, size):
        self.data = [None] * size

    def set(self, index, value):
        self.data[index] = value

    def get(self, index):
        return self.data[index]

    def show(self):
        return self.data


array = Array(5)

array.set(0, 10)
array.set(1, 20)

print(array.show())