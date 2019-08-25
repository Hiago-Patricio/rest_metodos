import auxiliary


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
    aproximation = 0.0000000000001

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