import auxiliary, function, derivative, math, importlib, os, json


# Recarrega o cache
def reload():
    try:
        os.system('rm -r ./__pycache__')
        importlib.reload(function)
        importlib.reload(derivative)
    except:
        pass


def start_bisection(a, b, error, func):
    a, b, error = auxiliary.n_float(a, b, error)
    auxiliary.write(func, 'function')
    reload()
    return method_bisection(a, b, error)


def start_false_position(a, b, error, func):
    a, b, error = auxiliary.n_float(a, b, error)
    auxiliary.write(func, 'function')
    reload()
    return method_false_position(a, b, error)


def start_newton_raphson(x, error, func, derivative):
    x, error = auxiliary.n_float(x, error)
    auxiliary.write(func, 'function')
    auxiliary.write(derivative, 'derivative')
    reload()
    return method_newton_raphson(x, error)


def start_secant(x0, x1, error, func):
    x0, x1, error = auxiliary.n_float(x0, x1, error)
    auxiliary.write(func, 'function')
    reload()
    return method_secant(x0, x1, error)


def method_bisection(a: float, b: float, error: float):
    while True:
        f_a = function.f(a)
        f_a = auxiliary.rounding(f_a, error)
        f_b = function.f(b)
        f_b = auxiliary.rounding(f_b, error)

        if math.fabs(f_a) <= error:
            return auxiliary.convert_json('x', a)
        elif math.fabs(f_b) <= error:
            return auxiliary.convert_json('x', b)
        elif f_a * f_b < 0:
            x = (a + b) / 2
            f_x = function.f(x)
            f_x = auxiliary.rounding(f_x, error)
            if f_a * f_x < 0:
                b = x
            else:
                a = x
        else:
            return auxiliary.convert_json('x', 'Inválido')


def method_false_position(a: float, b: float, error: float):
    while True:
        f_a = function.f(a)
        f_b = function.f(b)

        if math.fabs(f_a) <= error:
            return auxiliary.convert_json('x', a)
        elif math.fabs(f_b) <= error:
            return auxiliary.convert_json('x', b)
        elif f_a * f_b < 0:
            x = (a * f_b - b * f_a) / (f_b - f_a)
            f_x = function.f(x)
            if f_a * f_x < 0:
                b = x
            else:
                a = x
        else:
            return auxiliary.convert_json('x', 'Inválido')


def method_newton_raphson(x: float, error: float):
    while True:
        f_x = function.f(x)
        f_x = auxiliary.rounding(f_x, error)
        if math.fabs(f_x) <= error:
            return auxiliary.convert_json('x', x)
        f_dx = derivative.f(x)
        f_dx = auxiliary.rounding(f_dx, error)
        x = x - f_x / f_dx
        x = auxiliary.rounding(x, error)


def method_secant(x0: float, x1: float, error: float):
    while True:
        f_x0 = function.f(x0)
        f_x0 = auxiliary.rounding(f_x0, error)
        f_x1 = function.f(x1)
        f_x1 = auxiliary.rounding(f_x1, error)
        x = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)
        x = auxiliary.rounding(x, error)
        f_x = function.f(x)
        f_x = auxiliary.rounding(f_x, error)
        if (math.fabs(f_x0) <= error):
            return auxiliary.convert_json('x', x0)
        elif (math.fabs(f_x1) <= error):
            return auxiliary.convert_json('x', x1)
        elif (math.fabs(f_x) <= error):
            return auxiliary.convert_json('x', x)
        x0 = x1
        x1 = x