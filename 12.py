letters_with_holes = 'abdegopq'


def count_holes_and_nonholes(string):
    holes = sum(1 for c in string if c in letters_with_holes)
    nonholes = sum(1 for c in string if c.isalpha() and c not in letters_with_holes)
    return holes, nonholes


def words_with_two_or_more_holes(string):
    return [word for word in string.split() if sum(1 for c in word if c in letters_with_holes) >= 2]


if __name__ == "__main__":
    string = input("Введите строку: ")

    holes, nonholes = count_holes_and_nonholes(string)
    words = words_with_two_or_more_holes(string)

    print(f"Количество букв с отверстиями: {holes}")
    print(f"Количество букв без отверстий: {nonholes}")
    print(f"Слова, имеющие две и более буквы с отверстиями: {words}")
