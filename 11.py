lst = list(map(int, input('Введите числа, разделенные пробелами: ').split()))

command = input('Введите команду:')
if command[0] not in ['L', 'R']:
    print("Некорректная команда. Пожалуйста, введите команду в формате 'L3' или 'R5'")
    command = input('Введите команду:')

num_positions = int(command[1:])

if command[0] == 'R':
    lst = lst[-num_positions:] + lst[:-num_positions]
elif command[0] == 'L':
    lst = lst[num_positions:] + lst[:num_positions]

print(lst)
