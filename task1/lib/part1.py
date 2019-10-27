import numpy as np

def calculate_unknown_grades_kNN(
    input_user,             # номер пользователя, для которого вычисляются оценки фильмов
    grades,                 # матрица оценок
    sim,                    # матрица расстояний между пользователями
    k                       # параметр k для метода kNN
    ):

    n = grades.shape[0]     # количество пользователей
    m = grades.shape[1]     # количество фильмов для оценки
    result = list()         # Выходной список. Каждый элемент - пара: <номер фильма без оценки, вычисленная оценка>

    best_fitting_users = np.argsort(-sim) # матрица, содержащая для каждого пользователя список номеров пользователей по убыванию расстояния: вначале номер наиболее близкого, затем номер второго по дистанции и т.д.
    means = np.empty(n)                   # массив средних арифметических оценок пользователей
    for i in range(n):
        values = grades[i][(grades[i] != -1).nonzero()]
        means[i] = round(values.mean(), 3)

    for film_num in range(m):
        if grades[input_user][film_num] == -1:

            # строим k наиболее близких пользователей среди оценивших фильм
            k_best_fitting = list()
            for cur_user in best_fitting_users[input_user]:
                if grades[cur_user][film_num] != -1:
                    k_best_fitting.append(cur_user)
                if len(k_best_fitting) == k:
                    break

            # если не удается вычислить оценку, ставим null и идем дальше
            if len(k_best_fitting) < k or k_best_fitting[k - 1] == -1:
                result.append((film_num, None))
                continue

            # вычисляем и фиксируем оценку
            numerator = 0
            denominator = 0
            for cur_user in k_best_fitting:
                denominator += sim[input_user][cur_user]
                numerator += sim[input_user][cur_user] * (grades[cur_user][film_num] - means[cur_user])
                numerator = round(numerator, 3)
            value = means[input_user] + round(numerator/denominator, 3)
            
            result.append((film_num, value))
    
    return result
