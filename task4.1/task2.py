
string = input("Введите строку: ")
nums_raw = input("Введите позиции в строке (разделенные пробелом, нумерация с 0): ")
numbers = list(map(int, nums_raw.split()))
to_print = "Cимволы, находящихся на заданных позициях:"

try:
    # with list comprehensions
    letters_str = [string[i] for i in numbers]
    print(to_print, ''.join(letters_str))

    # without list comprehensions 1
    letters_str = []
    for i in numbers:
        letters_str.append(string[i])
    print(to_print, ''.join(letters_str))

    # without list comprehensions 2
    letters_str = map(lambda x: string[x], numbers)
    print(to_print, ''.join(letters_str))
    
except IndexError:
    print("Некорректный номер позиции присутствует в списке")
