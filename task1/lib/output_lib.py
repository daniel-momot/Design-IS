
def do_output(users, movies, grades_list, filename):
    with open(filename, 'w') as f:
        print('{', file=f)
        for user_num in range(len(users)):
            print('  {', file=f)
            print('     "user": ' + str(user_num) + ',', file=f)
            print('     "1": {', file=f)
            for i, grade in enumerate(grades_list[user_num]):
                if i != len(grades_list[user_num]) - 1:
                    print('          "' + movies[grade[0]] + '": ' + str(round(grade[1], 1)) + ',', file=f)
                if i == len(grades_list[user_num]) - 1:
                    print('          "' + movies[grade[0]] + '": ' + str(round(grade[1], 1)), file=f)
            print('          }', file=f)
            print('  },', file=f)
        print('}', file=f)
    return
   
       
