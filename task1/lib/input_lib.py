import numpy as np
import sys


def read_data_from_file(filename, possible_values):
    try:
        with open(filename,"r") as file:
            
            movies_names = file.readline().strip().split(', ')
            movies_names.pop(0)
            
            users_names = list()
            users_info_raw = [line.strip().split(', ') for line in file] # список списков слов
            data_shape = [len(users_info_raw), len(users_info_raw[0]) - 1]
            data = np.empty(data_shape)
            for i, user_info in enumerate(users_info_raw):
                users_names.append(user_info.pop(0))
                for j, data_piece in enumerate(user_info):
                    data[i][j] = possible_values[data_piece]
        ret_dict = {
            'users': users_names,
            'movies': movies_names,
            'data': data
        }
        return ret_dict
    except BaseException:
        sys.exit("File " + filename + " has incorrect format!")

def verify_input(*args):
    if len(args) == 0:  return None

    arg1 = args[1]
    for arg in args:
        if arg['movies'] != arg1['movies']:
            sys.exit("unconsistent movies names!")
        if arg['users'] != arg1['users']:
            sys.exit("unconsistent users names!")
        if arg['data'].shape != arg1['data'].shape:
            sys.exit("unconsistent data arrays dimensions!")
        for i in range(arg1['data'].shape[0]):
            for j in range(arg1['data'].shape[1]):
                b1 = arg1['data'][j][j] == -1
                b2 = arg['data'][j][j] == -1
                if b1 != b2:
                    sys.exit("unconsistent data arrays empty values!")

    res = [arg1['movies'], arg1['users']]        
    for arg in args:
        res.append(arg['data'])
    return res
    
       
