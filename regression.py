import math, auxiliary


def start_linear(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_linear(x, y)


def method_linear(x: list, y: list):
    n = len(x)
    somatorio_x = 0
    somatorio_x2 = 0
    somatorio_y = 0
    somatorio_xy = 0

    for i, j in zip(x, y):
        somatorio_x += i
        somatorio_x2 += i**2
        somatorio_y += j
        somatorio_xy += j * i

    media_x = somatorio_x / n
    media_x2 = somatorio_x2 / n
    media_y = somatorio_y / n
    media_xy = somatorio_xy / n

    m = (media_x*media_y - media_xy) / (media_x**2 - media_x2)
    b = media_y - media_x * m

    equacao = str(m) + "*x"
    if b >= 0:
        equacao += "+"
    else:
        equacao += "-"
    equacao += str(math.fabs(b))
    return auxiliary.convert_json("equacao", equacao)