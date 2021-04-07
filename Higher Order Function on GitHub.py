def add(a):
    def func(b):
        return a + b

    return func

twoMore = add(2)
x = 10
xPlusTwo = twoMore(x)
print(xPlusTwo)


def mult(a):
    def func(b):
        return a * b

    return func


timesTheOther = mult(4)
x = 2
xTimesA = timesTheOther(x)


def func(a, b):
    return a + b


x = map(func, ('dog', 'cat', 'fish'), ('kangaroo', 'koala', 'anteater'))

print(x)

print(list(x))

jersey_number = [2, 3, 19, 22, 38, 89]


def func(x):
    if x >= 38:
        return True
    else:
        return False


players = filter(func, jersey_number)

for x in players:
    print(x)
