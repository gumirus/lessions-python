# def bubble_sort(arr):
#    n = len(arr)
#    #Проходим по каждому элементу массива
#    for i in range(n):
#    for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         print(arr)

# a = [1, 5, 4, 2, 3, 6, 5, 4]
# bubble_sort(a) print(a)


# Merge sort

# надо будет посмотреть запись
# def merge(left, right):
#         merged = []
#         i = j = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 merged.append(left[i])
#                 i += 1
#             else:
#                 merged.append(right[j])
#                 j += 1
#         while i < len(left):
#             merged.append(left[i])
#             i += 1

#         while j < len(right):
#             merged.append(right[j])
#             j += 1
            
#         return merged
#     return merge_sort_recursive(arr)

# def new_func():
#     def quick_sort(arr):
#       if len(arr) <= 1:
#          return arr

#       pivot = arr[0]
#       left = []
#       right = []

#       for element in arr[1:]:
#           if pivot > element:
#               left.append(element)
#           else:
#               right.append (element)

#       return quick_sort(left) + [pivot] + quick_sort(right)

#       my_list - [64, 25, 12, 22, 11]
#       sorted_list = quick_sort(my_list) 
#       print(sorted_list)

#     a = [1, 5, 4, 2, 3, 6, 5, 4] 
#     sorted_arr = sorted(a)
#     print(sorted_arr)

#     sorted_arr = sorted(a, reverse=True)
#     print(sorted_arr)

#     a = [1, -4, 5, -7, 9, 2]
#     sorted_arr = sorted(a, key=abs)
#     print(sorted_arr)

#     def sort_key(e):
#       return e[1]

#     l1 = [(1, 2, 3), (2, 1, 3), (11, 4, 2), (9, 1, 3)]

#     print(sorted(l1))
#     print(sorted(l1, key=sort_key))

# return new_func()

# Создание и доступ к элементам двумерного списка
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a[1][1])  # Выводит второй элемент второго списка (5)
print(a[2][0])  # Выводит первый элемент третьего списка (7)

# Создание двумерного списка с использованием цикла
a = 3
mas = [[0] * a for _ in range(a)]
print(mas)

# Создание двумерного списка с использованием метода append
a = 2
mas = []
for _ in range(a):
    mas.append([1] * a)
print(mas)

# Создание двумерного списка с указанным значением
val = 1
M, N = 4, 5
x = [[val for _ in range(N)] for _ in range(M)]
print(x)

# Создание двумерного списка с определенным значением
a = 3
mas = [[2] * a for _ in range(a)]
print(mas)

# Создание двумерного списка с помощью ввода пользователя
a = int(input())
mas = []
for _ in range(a):
    mas.append(list(map(int, input().split())))
print(mas)

mas = [list(map(int, input().split())) for _ in range(int(input()))]
print(mas)

# Изменение и работа с элементами списка
mas = [[1, 2, 3], [4, 5, 6]]

mas[0].append(10)  # Добавляет элемент 10 в первый список
print(mas)

mas.append([5, 2, 3])  # Добавляет список [5, 2, 3] в конец
print(mas)

mas[0].remove(3)  # Удаляет элемент 3 из первого списка
print(mas)

a = [[1, 2, 31, [4, 5, 6], [7, 8, 9]]]

for row in a:
    for elem in row:
        print(elem)

def printMass(mass):
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            print("{:4d}".format(mass[i][j]), end='')
        print()

printMass(a)

# ---------------------------------

mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end='')
    print()

mas = [[1, 2, 31, [4, 5, 61]], [7, 8, 911]]

for i in mas:
    print(' '.join(list(map(str, i))))

mas = [[1, 2, 31, [4, 5, 61]], [7, 8, 911]]
string = 2
for i in mas[string - 1]:
    print(i, end='')
print('\n')

mas = [[1, 2, 3], [4, 5, 61], [7, 8, 911]]
column = 2
for i in mas:
    print(i[column - 1], end='')

mas = [[1, 2, 31, [4, 5, 61]], [7, 8, 911]]
column = [row[2] for row in mas]
print(column)

# -----------------------------

mas = [[2, 4, 7, 3], [4, 5, 6, 9], [1, 8, 4, 2], [7, 8, 4, 7]]

mas[0].sort()
print(mas)

mas2 = []
for i in mas:
    mas2.append(sorted(i))
print(mas2)

mas = [[2, 4, 7, 3], [4, 5, 6, 91, [1, 8, 4, 2], [7, 8, 4, 7]]]
mas2 = [i2 for i in mas for i2 in i]

mas = sorted(mas2)

for x in range(0, len(mas), 4):
    e_c = mas[x : 4 + x]
    print(list(e_c))
# ----------------------------

def row_sums(matrix):
    row_sums = []
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums

matrix = [[1, 2, 3], [4, 8, 10], [11, 15, 17]]
print(row_sums(matrix))

def is_palindrome(matrix):
    for row in matrix:
        reversed_row = row[::-1]
        if row != reversed_row:
            return False
    return True

matrix = [[1, 2, 1], [1, 2, 3],]
result = is_palindrome(matrix)
print(result)
