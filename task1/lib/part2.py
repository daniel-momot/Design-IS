import numpy as np
import math as mt

def count_weight(grades, user, film, days, cond_days, places, cond_places):
    cnt = 0
    if days[user][film] in cond_days: cnt+=1
    if places[user][film] in cond_places: cnt+=1

    if cnt==1: return 2
    elif cnt:  return 4
    else:      return 1


def find_best(grades, sim, k, input_user, days, cond_days, places, cond_places):
    '''
    Вычисление отсутствующих оценок методом user-based kNN + условия. cond_days, cond_places - lists!
    :rtype: list() of floats
    :param numpy matrix grades: матрица оценок
    :param numpy matrix sim: матрица расстояний между пользователями
    :param int k: параметр k для метода kNN
    :param int input_user: номер пользователя, для которого вычисляются оценки фильмов
    '''

    n = grades.shape[0]     # количество пользователей
    m = grades.shape[1]     # количество фильмов для оценки
    results = list()         # Выходной список. Каждый элемент - пара: <номер фильма без оценки, вычисленная оценка>

    if input_user < 0 or input_user >= n:
        print("Incorrect user number provided!")
        exit()

    # Матрица, содержащая для каждого пользователя список номеров пользователей по убыванию расстояния: вначале номер наиболее близкого, затем номер второго по дистанции и т.д.
    best_fitting_users = np.argsort(-sim)

    # Находим для каждого пользователя среднее арифметическое его оценок
    means = np.empty(n)
    for i in range(n):
        values = grades[i][(grades[i] != -1).nonzero()]
        means[i] = round(values.mean(), 3)

    # Для всех непосмотренных фильмов вычисляем оценки (с учетом условий)
    for film_num in range(m):
        if grades[input_user][film_num] == -1:

            # Строим k наиболее близких пользователей среди оценивших фильм
            k_best_fitting = list()
            for cur_user in best_fitting_users[input_user]:
                if grades[cur_user][film_num] != -1:
                    k_best_fitting.append(cur_user)
                if len(k_best_fitting) == k:
                    break

            # если не удается вычислить оценку, ставим null и идем дальше
            if len(k_best_fitting) < k or k_best_fitting[k - 1] == -1:
                results.append((film_num, None))
                continue

            # вычисляем и фиксируем оценку
            numerator = 0
            denominator = 0
            for cur_user in k_best_fitting:
                weight = count_weight(grades, cur_user, film_num, days, cond_days, places, cond_places)
                numerator += weight * round(sim[input_user][cur_user] * (grades[cur_user][film_num] - means[cur_user]), 3)
                denominator += weight * sim[input_user][cur_user]
            value = means[input_user] + round(numerator/denominator, 3)

            results.append((film_num, value))

    # Среди фильмов с вычисленной оценкой выбираем наилучший
    best = results[0]
    for result in results:
        if result[1] > best[1]:
            best = result

    return best
