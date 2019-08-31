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
    digits = int(math.ceil(math.fabs(math.log10(aproximation)))+1)
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


def repeated_value(x: list):
    sorted(x)
    for i in range(len(x) - 1):
        if x[i] == x[i+1]:
            return True
    return False


def position(x, lista: list):
    for i in range(len(lista)):
        if x == lista[i]:
            return i
    return None


def repetead_amount(x, lista: list):
    qtd = 0
    for i in lista:
        if x == i:
            qtd += 1
    return qtd


z_horizontal = [
0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09
]
z_vertical = [
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9
]
z_table = [
0.0000,0.0040,0.0080,0.0120,0.0160,0.0199,0.0239,0.0279,0.0319,0.0359,
0.0398,0.0438,0.0478,0.0517,0.0557,0.0596,0.0636,0.0675,0.0714,0.0753,
0.0793,0.0832,0.0871,0.0910,0.0948,0.0987,0.1026,0.1064,0.1103,0.1141,
0.1179,0.1217,0.1255,0.1293,0.1331,0.1368,0.1406,0.1443,0.1480,0.1517,
0.1554,0.1591,0.1628,0.1664,0.1700,0.1736,0.1772,0.1808,0.1844,0.1879,
0.1915,0.1950,0.1985,0.2019,0.2054,0.2088,0.2123,0.2157,0.2190,0.2224,
0.2257,0.2291,0.2324,0.2357,0.2389,0.2422,0.2454,0.2486,0.2517,0.2549,
0.2580,0.2611,0.2642,0.2673,0.2704,0.2734,0.2764,0.2794,0.2823,0.2852,
0.2881,0.2910,0.2939,0.2967,0.2995,0.3023,0.3051,0.3078,0.3106,0.3133,
0.3159,0.3186,0.3212,0.3238,0.3264,0.3289,0.3315,0.3340,0.3365,0.3389,
0.3413,0.3438,0.3461,0.3485,0.3508,0.3531,0.3554,0.3577,0.3599,0.3621,
0.3643,0.3665,0.3686,0.3708,0.3729,0.3749,0.3770,0.3790,0.3810,0.3830,
0.3849,0.3869,0.3888,0.3907,0.3925,0.3944,0.3962,0.3980,0.3997,0.4015,
0.4032,0.4049,0.4066,0.4082,0.4099,0.4115,0.4131,0.4147,0.4162,0.4177,
0.4192,0.4207,0.4222,0.4236,0.4251,0.4265,0.4279,0.4292,0.4306,0.4319,
0.4332,0.4345,0.4357,0.4370,0.4382,0.4394,0.4406,0.4418,0.4429,0.4441,
0.4452,0.4463,0.4474,0.4484,0.4495,0.4505,0.4515,0.4525,0.4535,0.4545,
0.4554,0.4564,0.4573,0.4582,0.4591,0.4599,0.4608,0.4616,0.4625,0.4633,
0.4641,0.4649,0.4656,0.4664,0.4671,0.4678,0.4686,0.4693,0.4699,0.4706,
0.4713,0.4719,0.4726,0.4732,0.4738,0.4744,0.4750,0.4756,0.4761,0.4767,
0.4772,0.4778,0.4783,0.4788,0.4793,0.4798,0.4803,0.4808,0.4812,0.4817,
0.4821,0.4826,0.4830,0.4834,0.4838,0.4842,0.4846,0.4850,0.4854,0.4857,
0.4861,0.4864,0.4868,0.4871,0.4875,0.4878,0.4881,0.4884,0.4887,0.4890,
0.4893,0.4896,0.4898,0.4901,0.4904,0.4906,0.4909,0.4911,0.4913,0.4916,
0.4918,0.4920,0.4922,0.4925,0.4927,0.4929,0.4931,0.4932,0.4934,0.4936,
0.4938,0.4940,0.4941,0.4943,0.4945,0.4946,0.4948,0.4949,0.4951,0.4952,
0.4953,0.4955,0.4956,0.4957,0.4959,0.4960,0.4961,0.4962,0.4963,0.4964,
0.4965,0.4966,0.4967,0.4968,0.4969,0.4970,0.4971,0.4972,0.4973,0.4974,
0.4974,0.4975,0.4976,0.4977,0.4977,0.4978,0.4979,0.4979,0.4980,0.4981,
0.4981,0.4982,0.4982,0.4983,0.4984,0.4984,0.4985,0.4985,0.4986,0.4986,
0.4987,0.4987,0.4987,0.4988,0.4988,0.4989,0.4989,0.4989,0.4990,0.4990,
0.4990,0.4991,0.4991,0.4991,0.4992,0.4992,0.4992,0.4992,0.4993,0.4993,
0.4993,0.4993,0.4994,0.4994,0.4994,0.4994,0.4994,0.4995,0.4995,0.4995,
0.4995,0.4995,0.4995,0.4996,0.4996,0.4996,0.4996,0.4996,0.4996,0.4997,
0.4997,0.4997,0.4997,0.4997,0.4997,0.4997,0.4997,0.4997,0.4997,0.4998,
0.4998,0.4998,0.4998,0.4998,0.4998,0.4998,0.4998,0.4998,0.4998,0.4998,
0.4998,0.4998,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,
0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,
0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,0.4999,
0.5000,0.5000,0.5000,0.5000,0.5000,0.5000,0.5000,0.5000,0.5000,0.5000
]


def z_critico(num: float):
    i = 0
    while i < len(z_table) and z_table[i] < num:
        i+= 1
    return z_horizontal[i % 10] + z_vertical[int(i / 10)]


t_horizontal = [
0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.001
]
t_vertical = [
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 60, 120
]
t_table = [
0.158,0.325,0.51,0.727,1,1.376,1.963,3.078,6.314,12.706,31.821,63.657,636.619,
0.142,0.289,0.445,0.617,0.816,1.061,1.386,1.886,2.92,4.303,6.965,9.925,31.598,
0.137,0.277,0.424,0.584,0.765,0.978,1.25,1.638,2.353,3.182,4.541,5.541,12.924,
0.134,0.271,0.414,0.569,0.741,0.941,1.19,1.533,2.132,2.776,3.747,4.604,8.61,
0.132,0.267,0.408,0.559,0.727,0.92,1.156,1.476,2.015,2.571,3.365,4.032,6.869,
0.131,0.265,0.404,0.553,0.718,0.906,1.134,1.44,1.943,2.447,3.143,3.707,5.959,
0.13,0.263,0.402,0.549,0.711,0.896,1.119,1.415,1.895,2.365,2.365,3.499,5.408,
0.13,0.262,0.399,0.546,0.706,0.889,1.108,1.397,1.86,2.306,2.896,3.355,5.041,
0.129,0.261,0.398,0.543,0.703,0.883,1.1,1.383,1.833,2.262,2.821,3.25,4.781,
0.129,0.26,0.397,0.542,0.7,0.879,1.093,1.372,1.812,2.228,2.764,3.169,4.587,
0.129,0.26,0.396,0.54,0.697,0.876,1.088,1.363,1.796,2.201,2.718,3.106,4.437,
0.128,0.259,0.395,0.539,0.695,0.873,1.083,1.356,1.782,2.179,2.681,3.055,4.318,
0.128,0.259,0.394,0.538,0.694,0.87,1.079,1.35,1.771,2.16,2.65,3.012,4.221,
0.128,0.258,0.393,0.537,0.692,0.868,1.076,1.345,1.761,2.145,2.624,2.977,4.14,
0.128,0.258,0.393,0.536,0.691,0.866,1.074,1.341,1.753,2.131,2.602,2.947,4.073,
0.128,0.258,0.392,0.535,0.69,0.865,1.071,1.337,1.746,2.12,2.583,2.921,4.015,
0.128,0.257,0.392,0.534,0.689,0.863,1.069,1.333,1.74,2.11,2.567,2.898,3.965,
0.127,0.257,0.392,0.534,0.688,0.862,1.067,1.33,1.734,2.101,2.552,2.878,3.922,
0.127,0.257,0.391,0.533,0.688,0.861,1.066,1.328,1.729,2.093,2.539,2.861,3.883,
0.127,0.257,0.391,0.533,0.687,0.86,1.064,1.325,1.725,2.086,2.528,2.845,3.85,
0.127,0.257,0.391,0.532,0.686,0.859,1.063,1.323,1.721,2.08,2.518,2.831,3.819,
0.127,0.256,0.39,0.532,0.686,0.858,1.061,1.321,1.717,2.074,2.508,2.819,3.792,
0.127,0.256,0.39,0.532,0.685,0.858,1.06,1.319,1.714,2.069,2.5,2.807,3.767,
0.127,0.256,0.39,0.531,0.685,0.857,1.059,1.318,1.711,2.064,2.492,2.797,3.745,
0.127,0.256,0.39,0.531,0.684,0.856,1.058,1.316,1.708,2.06,2.485,2.787,3.726,
0.127,0.256,0.39,0.531,0.684,0.856,1.058,1.315,1.706,2.056,2.479,2.779,3.707,
0.127,0.256,0.389,0.531,0.684,0.856,1.057,1.314,1.703,2.052,2.473,2.771,3.69,
0.127,0.256,0.389,0.53,0.683,0.856,1.056,1.313,1.701,2.048,2.467,2.763,3.674,
0.127,0.256,0.389,0.53,0.683,0.854,1.055,1.311,1.699,2.045,2.462,2.756,3.659,
0.127,0.256,0.389,0.53,0.683,0.854,1.055,1.31,1.697,2.042,2.457,2.75,3.646,
0.126,0.255,0.388,0.529,0.681,0.851,1.05,1.303,1.684,2.021,2.423,2.704,3.551,
0.126,0.254,0.387,0.527,0.679,0.848,1.046,1.296,1.671,2,2.39,2.66,3.46,
0.126,0.254,0.386,0.526,0.677,0.845,1.041,1.289,1.658,1.98,2.358,2.617,3.373
]


def t_critico(free: int, sig: float):
    i = 0
    while i < len(t_vertical) and t_vertical[i] < free:
        i += 1

    j = len(t_horizontal) - 1
    while j >= 0 and t_horizontal[j] < sig:
        j -= 1

    return t_table[i*len(t_horizontal)+j]