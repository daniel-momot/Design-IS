def pipeline(func, val):
    for f in func:
        val = f(val)
    return val

def pipeline_each(func, obj):
    for val in obj:
        yield pipeline(func, val)

# Пример применения: вывод нечетных чисел

func = [ lambda x: 2 * x, lambda x: x + 1]

val = range(10)
for res in pipeline_each(func, val):
    print(res)
