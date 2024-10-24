# Первое задание
import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b
# g = fib_elem_gen()

# while True:
#     el = next(g)
#     print(el)
#     if el > 10:
#         break

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    return inner

@fib_coroutine
def my_genn():
    """Сопрограмма"""

    while True:
        number_of_fib_elem = yield
        print(f"Получено n: {number_of_fib_elem}")
        ... # создание элементов ряда Фибоначчи
        fib_gen = fib_elem_gen()
        #TODO: 
        # Сгенерировать список l, в который положить числа ряда Фиб 
        # по данном number_of_fib_elem (или с помощью yield from или с помощью itertools и функций оттуда 
        result = [next(fib_gen) for _ in range(number_of_fib_elem)] 
        yield result
        #l = [str(number_of_fib_elem)+":", 0, 1, 1] # example data
        #yield l

gen = my_genn()

print(gen.send(3))
print(gen.send(5))
print(gen.send(8))

#my_genn = fib_coroutine(my_genn)
#print(gen.send(5))

# Класс для второго задания
class FibonacchiLst:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
        self.fib_set = self._generate_fib_set(max(lst))
    def _generate_fib_set(self, max_value):
        fib_numbers = set()
        a,b = 0, 1
        while a <= max_value:
            fib_numbers.add(a)
            a, b = b, a + b
        return fib_numbers
    def __iter__(self):
        return self
    def __next__(self):
        while self.idx < len(self.lst):
            value = self.lst[self.idx]
            self.idx += 1
            if value in self.fib_set:
                return value
        raise StopIteration

# Пример использования
if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iterator = FibonacchiLst(lst)
    for num in fib_iterator:
        print(num)

# class EvenNumbersIterator():
    
#     def __init__(self, instance):
#         self.instance = instance   
#         self.idx = 0 # инициализируем индекс для перебора элементов
        
        
#     def __iter__(self):
#         return self # возвращает экземпляр класса, реализующего протокол итераторов
    
    
#     def __next__(self): # возвращает следующий по порядку элемент итератора
#         while True:
#             try:
#                 res = self.instance[self.idx] # получаем очередной элемент из iterable
                
#             except IndexError:
#                 raise StopIteration

#             if res % 2 == 0: # проверяем на четность элемента
#                 self.idx += 1 # если четный, возвращаем значение и увеличиваем индекс
#                 return res

#             self.idx += 1 # если нечетный, то просто увеличиваем индекс

    
# list(EvenNumbersIterator(range(10))) # [0, 2, 4, 6, 8]

