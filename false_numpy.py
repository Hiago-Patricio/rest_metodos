import crud_file, function_file, math, importlib, os, json

# Recarrega o cache
def reload():
    try:
        os.system('rm -r ./__pycache__')
        importlib.reload(function_file)
    except:
        pass


# É onde começa o programa
def start(a, b, error, function):
    a = float(a)
    b = float(b)
    error = float(error)
    crud_file.write(function, 'function_file.py')
    reload()
    # Arredondamento
    global aproximation
    aproximation = int(math.ceil(math.fabs(math.log10(error)))) + 1
    return str(method(a, b, error))


# É onde é feito a execução do método
aproximation = None
def method(a: float, b: float, error: float):
    global aproximation
    file_json = {}
    while True:
        # arredondamento
        f_a = round(function_file.f(a), aproximation)
        f_b = round(function_file.f(b), aproximation)
        x = round((a * f_b - b * f_a) / (f_b - f_a), aproximation)
        f_x = round(function_file.f(x), aproximation)
        if (math.fabs(f_a) <= error):
            file_json['x'] = str(a)
            return json.dumps(file_json, indent = 2)
        elif (math.fabs(f_b) <= error):
            file_json['x'] = str(b)
            return json.dumps(file_json, indent = 2)
        elif (math.fabs(f_x) <= error):
            file_json['x'] = str(x)
            return json.dumps(file_json, indent = 2)
        elif ((f_a * f_x) < 0):
            # arredondamento
            b = round(x, aproximation)
        elif ((f_b * f_x) < 0):
            # arredontamento
            a = round(x, aproximation)
        else:
            return file_json.format(None)