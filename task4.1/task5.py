def split_to_words(strr):
    words = strr.split(' ')
    i = 0
    n = len(words)
    while i < n:
        yield words[i]
        i += 1

strr = input("Введите строку из слов, разделенных пробелами: ")
a = map(lambda x: print(x), split_to_words(strr))
list(a)
