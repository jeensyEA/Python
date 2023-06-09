# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

def inputList(x: int, collection: str):
    output = list()
    for i in range(x):
        item = int(input(f'Введите для набора {collection} значение элемента [{i}]: '))
        output.append(item)
    return output


n = int(input('Введите количество элементов в наборе A: '))
A = inputList(n, 'A')
print('-' * 20)
m = int(input('Введите количество элементов в наборе B: '))
B = inputList(m, 'B')
print(f'\nA = {A}\nB = {B}\n' + '-' * 20)
result = list(set(A).intersection(set(B)))
result.sort()
print(f'В обоих наборах встречаются: {result}')
