import crud, function, derivative, math, importlib, os, json


# Recarrega o cache
def reload():
    try:
        os.system('rm -r ./__pycache__')
        importlib.reload(function)
        importlib.reload(derivative)
    except:
        pass


# Converte lista em float
def list_float(*num):
    res = [float(i) for i in num]
    return res


# Arredondamento para erro permitido
def rounding(num: float, error: float):
    digits = int(len(str(error)) - 2)
    return round(num, digits)


def convert_json(key, content):
    key = str(key)
    content = str(content)
    file_json = {key: content}
    return json.dumps(file_json, indent = 2)


def start_bisection(a, b, error, func):
    a, b, error = list_float(a, b, error)
    crud.write(func, 'function')
    return method_bisection(a, b, error)


def start_false_position(a, b, error, func):
    a, b, error = list_float(a, b, error)
    crud.write(func, 'function')
    return method_false_position(a, b, error)


def start_newton_raphson(x, error, func, derivative):
    x, error = list_float(x, error)
    crud.write(func, 'function')
    crud.write(derivative, 'derivative')
    return method_newton_raphson(x, error)


def start_secant(x0, x1, error, func):
    x0, x1, error = list_float(x0, x1, error)
    crud.write(func, 'function')
    return method_secant(x0, x1, error)


def method_bisection(a: float, b: float, error: float):
    while True:
        f_a = function.f(a)
        f_a = rounding(f_a, error)
        f_b = function.f(b)
        f_b = rounding(f_b, error)
        x = (a + b) / 2
        f_x = function.f(x)
        f_x = rounding(f_x, error)

        if math.fabs(f_a) <= error:
            return convert_json('x', a)
        elif math.fabs(f_b) <= error:
            return convert_json('x', b)
        elif math.fabs(f_x) <= error:
            return convert_json('x', x)
        elif (f_a * f_x) < 0:
            b = rounding(x, error)
        elif (f_b * f_x) < 0:
            a = rounding(x, error)
        else:
            return file_json.format(None)


def method_false_position(a: float, b: float, error: float):
    while True:
        f_a = function.f(a)
        f_a = rounding(f_a, error)
        f_b = function.f(b)
        f_b = rounding(f_b, error)
        x = (a * f_b - b * f_a) / (f_b - f_a)
        x = rounding(x, error)
        f_x = function.f(x)
        f_x = rounding(f_x, error)

        if math.fabs(f_a) <= error:
            return convert_json('x', a)
        elif math.fabs(f_b) <= error:
            return convert_json('x', b)
        elif math.fabs(f_x) <= error:
            return convert_json('x', x)
        elif (f_a * f_x) < 0:
            b = rounding(x, error)
        elif (f_b * f_x) < 0:
            a = rounding(x, error)
        else:
            return file_json.format(None)


def method_newton_raphson(x: float, error: float):
    while True:
        f_x = function.f(x)
        f_x = rounding(f_x, error)
        if math.fabs(f_x) <= error:
            return convert_json('x', x)
        f_dx = derivative.f(x)
        f_dx = rounding(f_dx, error)
        x = x - f_x / f_dx
        x = rounding(x, error)


def method_secant(x0: float, x1: float, error: float):
    while True:
        f_x0 = function.f(x0)
        f_x0 = rounding(f_x0, error)
        f_x1 = function.f(x1)
        f_x1 = rounding(f_x1, error)
        x = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)
        x = rounding(x, error)
        f_x = function.f(x)
        f_x = rounding(f_x, error)
        if (math.fabs(f_x0) <= error):
            return convert_json('x', x0)
        elif (math.fabs(f_x1) <= error):
            return convert_json('x', x1)
        elif (math.fabs(f_x) <= error):
            return convert_json('x', x)
        x0 = x1
        x1 = x