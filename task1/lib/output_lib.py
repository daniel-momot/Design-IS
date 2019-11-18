
def info2json(usernum, movies, grades, best, filename):
    print('{', file=filename)
    print('     "user": ' + str(usernum) + ',', file=filename)
    print('     "1": {', file=filename)
    for grade in grades:
        print('          "' + movies[grade[0]] + '": ' + str(round(grade[1], 3)) + ',', file=filename)
    print('          },', file=filename)
    print('     "2": {', file=filename)
    print('          "' + movies[best[0]] + '": ' + str(round(best[1], 3)) + ',', file=filename)
    print('          }', file=filename)
    print('}', file=filename)
    return
