def sort_string(s):
    s_list = list(s)
    s_list.sort()
    return ''.join(s_list)


user_string = input("Введите строку: ")

print(sort_string(user_string))
