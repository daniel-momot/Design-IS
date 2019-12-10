

def arifm_coroutine():
    cur = 0
    while True:
        inp = yield cur
        if inp != None:
            cur = inp
        cur += 1


c = arifm_coroutine()

for i in range(4):
    print(str(next(c)))

print(str(c.send(30)))

for i in range(3):
    print(str(next(c)))
