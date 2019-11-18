from lib.input_lib import read_from_file, verify_input
from lib.part1 import build_sim, count_grades
from lib.part2 import find_best
from lib.output_lib import info2json

poss_grades = {
    str(1): 1, str(2): 2, str(3): 3,
    str(4): 4, str(5): 5, str(-1): -1 }
poss_days = {
    'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4,
    'Fri': 5, 'Sat': 6, 'Sun': 7, str(-1): -1 }
poss_places = { 'h': 1, 'c': 2, 'v': 3, str(-1): -1 }

raw_grades = read_from_file("data.csv", poss_grades)
raw_days   = read_from_file("context_day.csv", poss_days)
raw_places = read_from_file("context_place.csv", poss_places)

movies, users, grades, days, places = verify_input(raw_grades, raw_days, raw_places)

sim = build_sim(grades)

# debug option
''' np.set_printoptions(threshold=sys.maxsize)
print(sim) '''

k = 4
with open('output-all.json', 'w') as file:
    for usernum in range(len(users)):
        ranks = count_grades(grades, sim, k, usernum)
        best = find_best(grades, sim, k, usernum, days, [poss_days['Sat'], poss_days['Sun']], places, [poss_places['h']])
        info2json(usernum, movies, ranks, best, file)
		
usernum = int(input("Input user number (0-39): "))
with open('output.json', 'w') as file:
    ranks = count_grades(grades, sim, k, usernum)
    best = find_best(grades, sim, k, usernum, days, [poss_days['Sat'], poss_days['Sun']], places, [poss_places['h']])
    info2json(usernum, movies, ranks, best, file)
