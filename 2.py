numbers = list(map(int, input("Введите числа через пробел: ").split()))
new_numbers = [num for num in numbers if num != 3]
print(new_numbers)
