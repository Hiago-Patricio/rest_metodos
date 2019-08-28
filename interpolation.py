import auxiliary, math, json


def start_lagrange(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_lagrange(x, y)


def start_newton_polynomial(x, d0):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    d0 = auxiliary.str_list(d0)
    d0 = auxiliary.list_float(d0)
    return method_newton_polynomial(x, d0)


def start_trigonometric(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_trigonometric(x, y)


def start_spline(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_spline(x, y)


def method_lagrange(x: list, y: list):
    '''
    :param x: lista que contém os valores de x
    :param y: lista que contém os valores de y
    :return:
    '''
    aproximation = 0.0001
    coefficients = []
    for x_i, y_i in zip(x, y):
        coef_aux = [1]
        denominator_aux = 1

        for x_j in x:
            if x_i != x_j:
                # Guarda o denominador
                denominator_aux *= x_i - x_j
                # Multiplica os polinômios (1)*(x - xj-1)(x - xj)
                coef_aux = auxiliary.polymul(coef_aux, [1, - x_j])

        coef_aux = auxiliary.polymulnum(y_i, coef_aux)
        coef_aux = auxiliary.polydivnum(denominator_aux, coef_aux)
        coefficients.append(coef_aux)

    resultado = []
    for coef_aux in coefficients:
        resultado = auxiliary.polyadd(resultado, coef_aux)
    resultado = auxiliary.printpoly(resultado, aproximation)
    return auxiliary.convert_json('equacao', resultado)


def method_newton_polynomial(x: list, d0: list):
    d = [d0]
    diff = 1
    poly = [1]
    aproximation = 0.0001

    for i in range(0, len(x) - 1):
        d_aux = []
        for j in range(0, len(d[i]) - 1):
            temp = d[i][j + 1] - d[i][j]
            temp /= x[j + diff] - x[j]
            d_aux.append(temp)
        d.append(d_aux)

        poly = auxiliary.polymul(poly, [1, -x[i]])
        poly_aux = auxiliary.polymulnum(d_aux[0], poly)
        if i == 0:
            res = auxiliary.polyadd([d0[0]], poly_aux)
        else:
            res = auxiliary.polyadd(res, poly_aux)
        diff += 1
    return auxiliary.printpoly(res, aproximation)


def method_trigonometric(x: list, y: list):
    n = len(x)
    m = int(n / 2)
    coef = 2 * math.pi / float(n)
    x_pi = auxiliary.polymulnum(coef, x)

    res = ''
    # A0
    calcA = calculationA(n, x_pi, y, 0)
    if calcA != 0:
        res += str(calculationA(n, x_pi, y, 0) / 2.0)

    # Caso par
    if n % 2 == 0:
        lim = m
    # Caso impar
    else:
        lim = m + 1

    # Ak*cos(k*x)+Bk*sen(k*x)
    for i in range(1, lim):
        calcA = calculationA(n, x_pi, y, i)
        if calcA > 0:
            res += '+' + str(calcA) + '*cos(' + str(i) + '*x)'
        elif calcA < 0:
            res += str(calcA) + '*cos(' + str(i) + '*x)'

        calcB = calculationB(n, x_pi, y, i)
        if calcB > 0:
            res += '+' + str(calcB) + '*sen(' + str(i) + '*x)'
        elif calcB < 0:
            res += str(calcB) + '*sen(' + str(i) + '*x)'

    # Am/2*cos(m/x)
    if n % 2 == 0:
        calcA = calculationA(n, x_pi, y, m)
        if calcA != 0:
            if calcA > 0:
                res += '+'
            res += str(calcA / 2.0) + '*cos(' + str(m) + '*x)'
    return res


# Calcula Aj
def calculationA(n: int, x_pi: list, y: list, j: int):
    sum = 0
    for i in range(n):
        sum += y[i] * math.cos(j * x_pi[i])
    sum *= 2.0 / n
    return round(sum, 3)


# Calcula Bj
def calculationB(n: int, x_pi: list, y: list, j: int):
    sum = 0
    for i in range(n):
        sum += y[i] * math.sin(j * x_pi[i])
    sum *= 2.0 / n
    return round(sum, 3)


def method_spline(x: list, y: list):
    res = {}
    aproximation = 0.0001
    for i in range(1, len(x)):
        first = auxiliary.polymulnum(y[i-1], [-1, x[i]])
        first = auxiliary.polydivnum(x[i] - x[i-1], first)

        second = auxiliary.polymulnum(y[i], [1, -x[i-1]])
        second = auxiliary.polydivnum(x[i] - x[i-1], second)

        polynomial = auxiliary.polyadd(first, second)
        res['S' + str(i) + '(x)'] = auxiliary.printpoly(polynomial, aproximation)
    return json.dumps(res, indent = 2)