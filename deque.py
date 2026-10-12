import numpy as np
from deque_interface import DequeInterface

class deque(DequeInterface):#создается класс дек
    def __init__(self, arraySize: int) -> None:
        self.arraySize = arraySize#запоминается размер

        self.myArray = np.empty(arraySize, dtype=np.int32)# создается сам массив. np.int32 означается что будут целые числа

        self.head = 0# место где начинается дек
        self.size = 0#количество числе лежащих внутри


    def accessByIndex(self, index: np.int32) -> np.int32:#получаем число по его номеру
        if index < 0 or index >= self.size:# спрашиваем существует ли такой номер
            raise IndexError("Такого элемента нет")

        realIndex = (self.head + index) % self.arraySize#нужна чтобы массив работал по кругу и ищет где реально лежит число

        return self.myArray[realIndex]#нашли нужное число


    def addToTail(self, num: np.int32) -> np.int32:#добавить число справа
        if self.size >= self.arraySize:#проверяется есть ли свободное место
            raise OverflowError("Deque заполнен")#дека заполнена

        tailIndex = (self.head + self.size) % self.arraySize#ищем место куда положить число справа

        self.myArray[tailIndex] = num# следовательно кладем в свободное если такое есть
        self.size += 1# чисел стало больше

        return np.int32(num)


    def addToHead(self, num: np.int32) -> np.int32:# добавить число в начало
        if self.size >= self.arraySize:#ищем  есть ли свободное место
            raise OverflowError("Deque заполнен")#если все занято - ошибка

        self.head = (self.head - 1) % self.arraySize# говорим что начало деки на одну ячейку раньше

        self.myArray[self.head] = num#кладем число в место head
        self.size += 1# добавили еще одно число

        return np.int32(num)# возвращаем добавленное число
# проверка
d = deque(5)# грубо говоря 5 коробочек

d.addToTail(10)# кладет числа 10 в конец и так последующие 3 команды
d.addToTail(20)
d.addToTail(30)

d.addToHead(5)#добавить число 5 слева

print(d.accessByIndex(0))
print(d.accessByIndex(1))
print(d.accessByIndex(2))
print(d.accessByIndex(3))