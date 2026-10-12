class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def get(self, index):
        current = self.head

        for i in range(index):
            current = current.next

        return current.value

    def show(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result


spisok = LinkedList()

spisok.add(10)
spisok.add(20)
spisok.add(30)

print(spisok.show())