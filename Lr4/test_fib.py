def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_3():
    gen = my_genn()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "Восемь первых членов ряда"

def test_fib_extreme_cases():
    gen = my_genn()
    assert gen.send(0) == [], "Пустой ряд для n = 0"
    assert gen.send(1) == [0], "Ряд с одним элементом для n = 1"

def test_fib_list_1():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == [0, 1, 2, 3, 5, 8, 1], "Фильтр чисел Фибоначчи"

def test_fib_list_2():
    lst = [10, 11, 12, 13]
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == [], "Нет чисел Фибоначчи в списке"