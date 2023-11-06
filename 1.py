numbers = [int(input("Введите число: ")) for _ in range(10)]
new_numbers = [numbers[i] + numbers[i + 1] for i in range(len(numbers) - 1)]
print(new_numbers)
