lst1 = list(map(int, input('Введите числа для первого списка через пробел: ').split()))
lst2 = list(map(int, input('Введите числа для второго списка через пробел: ').split()))

start, end = map(int, input('Введите начало и конец диапазона (включительно) через пробел: ').split())

start -= 1

temp_list = lst1[start: end]
temp_list.reverse()
lst2.extend(temp_list)
del lst1[start: end]

print(lst1)
print(lst2)
