from spisok import LinkedList


def test_add():
    spisok = LinkedList()

    spisok.add(10)
    spisok.add(20)
    spisok.add(30)

    assert spisok.show() == [10, 20, 30]


def test_get():
    spisok = LinkedList()

    spisok.add(10)
    spisok.add(20)
    spisok.add(30)

    assert spisok.get(1) == 20