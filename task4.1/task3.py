
text = input("Введите текст: ")
capitalize_letter = lambda tup: tup[1].upper() if tup[0] == 0 else tup[1].lower()
capitalize_sentence = lambda snt: ''.join(map(capitalize_letter, enumerate(snt)))
res = map(capitalize_sentence, text.split('.'))
print('.'.join(res))
