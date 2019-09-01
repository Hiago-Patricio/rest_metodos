import auxiliary, random, json


def start_bootstrap(amostra, vezes, conf):
    amostra = auxiliary.str_list(amostra)
    amostra = auxiliary.list_float(amostra)
    conf = round(float(conf), 4)
    vezes = int(vezes)
    return method_bootstrap(amostra, vezes, conf)


def start_jackknife(amostra, conf):
    amostra = auxiliary.str_list(amostra)
    amostra = auxiliary.list_float(amostra)
    conf = round(float(conf), 4)
    return method_jackknife(amostra, conf)


def method_bootstrap(amostra: list, vezes: int, conf:float):
    n = len (amostra)
    soma_total = []

    for i in range(vezes):
        aux = 0
        for i in range(n):
            aux += amostra[random.randrange(0, n)]
        aux /= n
        soma_total.append(aux)

    o_j = sum(soma_total)/vezes

    soma_o_j = 0
    for o_i in soma_total:
        soma_o_j += (o_i - o_j) ** 2

    soma_o_j /= vezes-1
    ep_o_j = soma_o_j ** 0.5
    zc = auxiliary.z_critico(conf/2)
    res = {}
    res['left'] = o_j - zc * ep_o_j
    res['right'] = o_j + zc * ep_o_j
    return json.dumps(res, indent = 2)


def method_jackknife(amostra: list, conf: float):
    n = len (amostra)
    soma_total = []
    for retirado in amostra:
        soma = 0
        for num in amostra:
            if retirado != num:
                soma += num
        soma_total.append(soma/(n-1))
    o_j = sum(soma_total)/n

    soma_o_j = 0
    for o_i in soma_total:
        soma_o_j += (o_i - o_j) ** 2

    soma_o_j /= n-1
    ep_o_j = soma_o_j ** 0.5
    zc = auxiliary.z_critico(conf/2)
    res = {}
    res['left'] = o_j - zc * ep_o_j
    res['right'] = o_j + zc * ep_o_j
    return json.dumps(res, indent = 2)