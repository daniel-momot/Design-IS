import numpy as np
import math as mt

def build_similarity_matrix(grades):
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
