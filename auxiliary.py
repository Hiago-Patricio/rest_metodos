import json

def write(function: str, name_file: str):
    file_function_content = '''
    from math import *
    
    def f(x):
        x = float(x)
        return {0}
    '''

    math_functions_convert = (
        ('log', 'log10'),
        ('ln', 'log'),
        ('sen(', 'sin(radians'),
        ('cos(', 'cos(radians'),
        ('tan(', 'tan(radians'),
        ('cot', 'atan'),
        ('csc', 'asin'),
        ('sec', 'acos'),
        ('^', '**'),
    )
    function = function.replace(' ','')
    function = function.replace('(', '((')
    function = function.replace(')', '))')
    for math_function in math_functions_convert:
        function = function.replace(math_function[0], math_function[1])
    with open(name_file + '.py', 'w+') as file_function:
        file_function.writelines(file_function_content.format(function))


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