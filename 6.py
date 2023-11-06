num = int(input('Введите число: '))
div = [i for i in range(1, num + 1) if num % i == 0]
print("Делители числа:", div)
