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


def write(function: str, name_file: str):
    function = function.replace(' ','')
    function = function.replace('(', '((')
    function = function.replace(')', '))')
    for math_function in math_functions_convert:
        function = function.replace(math_function[0], math_function[1])
    with open(name_file + '.py', 'w+') as file_function:
        file_function.writelines(file_function_content.format(function))