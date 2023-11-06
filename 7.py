numbers = list(map(int, input('Введите числа через пробел: ').split()))

sum_even = sum(num for num in numbers if num % 2 == 0)
sum_odd = sum(num for num in numbers if num % 2 != 0)

print('Сумма четных чисел:', sum_even)
print('Сумма нечетных чисел:', sum_odd)
