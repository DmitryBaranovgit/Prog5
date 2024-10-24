# Лабораторная работа №4

## Задание 1: Генерация чисел Фибоначчи с помощью сопрограмм

Данный проект реализует генерацию чисел ряда Фибоначчи с помощью сопрограмм

### Основные компоненты:
- **`fib_elem_gen()`** - генератор, который бесконечно возращает элементы ряда Фибоначчи.
- **`fib_coroutine()`** - декоратор для сопрограмм, который автоматически запускает генератор перед новой отправкой данных.
- **`my_genn()`** - сопрограмма, которая принимает количество требуемых чисел Фибоначчи и возращает соответствующий список чисел.

### Пример использования:
```python
gen = my_genn()
print(gen.send(3)) # Вернет [0, 1, 1]
print(gen.send(5)) # Вернет [0, 1, 1, 2, 3]
print(gen.send(8)) # Вернет [0, 1, 1, 2, 3, 5, 8, 13]
```
- **`fib_elem_gen()`** - генерирует числа Фибоначчи и используется в сопрограмме.

- **`my_genn()`** - при прлучении числа n генерирует список их первых n элементов ряда Фибоначчи и возращает его

## Задание 2: Класс для фильтрации чисел Фибоначчи из списка

Во втором задании реализован класс FibonacchiLst, который позволяет фильтровать список и выводить только те элементы, котопые принадлежат ряду Фибоначчи.

### Основные компоненты:
- **`__init__(lst)`** - конструктор, который принимает список и создает набор чисел Фибоеаччи до максимального элемента списка.
- **`__next__`** - метод, который возращает следующий элемент из списка, если он является числом Фибоначчи.

### Пример использования:
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
fib_iterator = FibonacchiLst(lst)
for num in fib_iterator:
  print(num) # Выведет только числа Фибоначчи: 0, 1, 1, 2, 3, 5, 8
```

- **`__generate_fib_set(max_value)`** - генерирует набор всех чисел Фибоначчи, не превышающих максимальное значение из преданного списка.
- **`__next__()`** - итерируется по списку и возращает только те числа, которые содержатся в ряду Фибоначчи.

# Результат:
[Основной код: gen_fib.py](/Lr4/gen_fib.py)

[Код с тестами: test_fib.py](/Lr4/test_fib.py)

![Задание 1](/Lr4/Lr4p1.png "Результат задания 1")

**Скриншот 1. Результат задания 1** 

![Задание 2](/Lr4/Lr4p2.png "Результат задания 2")

**Скриншот 2. Результат задания 2**
