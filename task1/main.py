from lib.input_lib import read_data_from_file, verify_input
from lib.similarity import build_similarity_matrix
from lib.part1 import calculate_unknown_grades_kNN



grades_to_set = {
    str(1): 1, str(2): 2, str(3): 3,
    str(4): 4, str(5): 5, str(-1): -1 }
days_of_week = {
    'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4,
    'Fri': 5, 'Sat': 6, 'Sun': 7, str(-1): -1 }
places_to_watch = { 'h': 1, 'c': 2, 'v': 3, str(-1): -1 }

raw_grades = read_data_from_file("data.csv", grades_to_set)
raw_days =   read_data_from_file("context_day.csv", days_of_week)
raw_places = read_data_from_file("context_place.csv", places_to_watch)

movies, users, grades, days, places = verify_input(raw_grades, raw_days, raw_places)

sim = build_similarity_matrix(grades)
# debug option
''' np.set_printoptions(threshold=sys.maxsize)
 print(sim) '''

k = 4
counted_grades = calculate_unknown_grades_kNN(0, grades, sim, k)
print(counted_grades)






                

                


              
 


