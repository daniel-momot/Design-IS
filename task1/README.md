- Для расчета оценок используется подход user-based коллаборативной фильтрации, метод kNN, k = 4.
- Для расчета оценок в определнных условиях используется тот же метод, но при расчете используются дополнительные веса: соблюдение условий.
Иначе говоря:
  - Если фильм посмотрен не в выходной и не дома (соблюдается 0 из 2 условий), оценке присваивается вес 1.
  - Если фильм посмотрен в выходной не дома, или же дома не в выходной (соблюдается 1 из 2 условий), оценке присваивается вес 2.
  - Если фильм посмотрен в выходной дома (соблюдается 2 из 2 условий), оценке присваивается вес 4.
