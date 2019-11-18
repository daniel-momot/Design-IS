import numpy as np
import math as mt

def build_sim(grades):
    '''
    Построение матрицы близости пользователей
    @rtype: numpy matrix
    @param numpy matrix grades: матрица оценок пользователей
    '''
    n = grades.shape[0]     # количество пользователей
    m = grades.shape[1]     # количество оценок у каждого пользователя

    grades_sq = grades ** 2
    graded = grades != -1

    sim = np.empty([n, n])  # выходная матрица [n x n] расстояний между пользователями в интервале []
    for i in range(n):
        for j in range(i, n):
            # номера фильмов, которые оценили оба пользователя
            nums = np.intersect1d(graded[i].nonzero(), graded[j].nonzero(), True)
            if i == j or len(nums) == 0:
                sim[i][j] = sim[j][i] = -1
            else:
                summ = np.dot(grades[i][nums], grades[j][nums])
                div1 = mt.sqrt(np.sum(grades_sq[i][nums]))
                div2 = mt.sqrt(np.sum(grades_sq[j][nums]))
                sim[i][j] = sim[j][i] = round(summ / (div1 * div2), 3)

    return sim

def count_grades( grades, sim, k, input_user ):
    '''
    Вычисление отсутствующих оценок методом user-based kNN
    @rtype: list() of floats
    @param numpy matrix grades: матрица оценок
    @param numpy matrix sim: матрица расстояний между пользователями
    @param int k: параметр k для метода kNN
    @param int input_user: номер пользователя, для которого вычисляются оценки фильмов
    '''

    n = grades.shape[0]     # количество пользователей
    m = grades.shape[1]     # количество фильмов для оценки
    result = list()         # Выходной список. Каждый элемент - пара: <номер фильма без оценки, вычисленная оценка>

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
