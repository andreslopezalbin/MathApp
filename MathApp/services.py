import random


def get_equation():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    res_out = x + y
    res = 'true'

    rand = random.randint(0, 2)
    if rand == 1:  # 66% of showing a fake result
        res_out += 1  # Fake result
        res = 'false'
    elif rand == 2:
        res_out -= 1  # Fake result
        res = 'false'

    equation = str(x) + ' + ' + str(y) + ' = ' + str(res_out)
    return {'equation': equation, 'res': res}
