
import time
import math

def get_random(strr):
    seed = int(strr) if (strr != '') else int(round(time.time())) # нормированное текущее время в секундах
    for i in range(3):
        seed = math.log(abs(seed))      # пропускаем первые "не очень рандомные" числа
        
    while True:
        yield seed
        seed = math.log(abs(seed))

strr = input("Введите начальное значение для ГПС (или просто нажмите Enter): ")

a = map(lambda x: print(x), get_random(strr))
list(a)
