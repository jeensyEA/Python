# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input("Введите N: "))

arr = []
for i in range(N):
    arr.append(int(input(f"Введите {i+1} число:")))
search = int(input(f"Введите искомое число:"))

index_min = 0
for i in range(N):
    if abs(arr[i]-search) < abs(arr[index_min]-search):
        index_min = i
print(arr)
print(f"Самый близкий элемент: {arr[index_min]}")