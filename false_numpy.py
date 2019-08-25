import math

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