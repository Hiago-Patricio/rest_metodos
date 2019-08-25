import json, math

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


# Arredondamento para erro permitido
def rounding(num: float, aproximation: float):
    digits = int(math.ceil(math.fabs(math.log10(aproximation))))
    return round(num, digits)


def convert_json(key, content):
    key = str(key)
    content = str(content)
    file_json = {key: content}
    return json.dumps(file_json, indent = 2)


# Converte string para lista de float
# input esperado: '1,2,3,4'
def str_list(x):
    x = x.replace(' ', '')
    x = x.split(',')
    x = [float(i) for i in x]
    return x


# Converte n elementos em float
def n_float(*num):
    res = [float(i) for i in num]
    return res


# Converte os elementos da lista em float
def list_float(coefficients: list):
    res = []
    for num in coefficients:
        res.append(float(num))
    return res


'''
Deve-se armazenar os coeficientes de modo a armazenar na ordem do maior grau de monômio ao menor para as funções que 
dependem disso. Ex: x^2 - 2 = [1, 0, -2]
'''

def polymulnum(number: float, coefficients: list):
    '''
    :param coefficients: lista que contém os coeficientes
    :param number: número pelo qual deve-se multiplicar a lista
    :return: resultado da multiplicação de coefficients e number
    '''
    coefficients = list_float(coefficients)
    res = []
    for coefficient_iterator in coefficients:
        res.append(coefficient_iterator * number)
    return res


def polydivnum(number: float, coefficients: list):
    '''
    :param coefficients: lista que contém os coeficientes
    :param number: número pelo qual deve-se multiplicar a lista
    :return: resultado da divisão de coefficients e number
    '''
    coefficients = list_float(coefficients)
    res = []
    for coef in coefficients:
        res.append(coef / number)
    return res


# Multiplica polinômios em forma de listas
def polymul(first: list, second: list):
    first = list_float(first)
    second = list_float(second)
    res = [0] * (len(first) + len(second) - 1)
    for i in range(len(first)):
        for j in range(len(second)):
            res[i+j] += first[i]*second[j]
    return res


# Soma polinômios em forma de listas
def polyadd(first: list, second: list):
    first = list_float(first)
    second = list_float(second)

    if len(first) >= len(second):
        res = first
        for i, num in zip(range(len(second)), second):
            position = len(first) - len(second) + i
            res[position] += num
    else:
        res = second
        for i, num in zip(range(len(first)), first):
            position = len(second) - len(first) + i
            res[position] += num

    return res


# Imprime o polinômio
def printpoly(coefficients: list, aproximation: float):
    res = ''
    greatest_exponent = len(coefficients) - 1
    coefficients = [rounding(coef, aproximation) for coef in coefficients]
    for coef, exponent in zip(coefficients, range(greatest_exponent, -1, - 1)):
        if math.fabs(coef) >= aproximation:
            if coef > 0:
                res += '+'
            res += str(coef)
            if exponent != 0:
                res += '*x^' + str(exponent)

    if res == '':
        res = 'None'
    return res