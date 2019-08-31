import auxiliary, json


def start_normal(dpp, n, media, conf):
    dpp, n, media, conf = auxiliary.n_float(dpp, n, media, conf)
    return method_normal(dpp, n, media, conf)


def start_t_student(amostra, conf):
    amostra = auxiliary.list_float(auxiliary.str_list(amostra))
    conf = float(conf)
    return method_t_student(amostra, conf)


def start_populacional(sucesso, total, conf):
    sucesso, total, conf = auxiliary.n_float(sucesso, total, conf)
    return method_populacional(sucesso, total, conf)


def method_normal(dpp:float, n:float, media:float, conf:float):
    res= {}
    conf /= 2
    res['left'] = media - auxiliary.z_critico(conf) * dpp / n ** 0.5
    res['right'] = media + auxiliary.z_critico(conf) * dpp / n ** 0.5
    return json.dumps(res, indent = 2)


def method_t_student(amostra:list, conf: float):
    n = len(amostra)
    media = sum(amostra)/n
    s = 0
    for i in amostra:
        s += (i - media) ** 2
    s = (s / (n-1)) ** 0.5
    sig = round(1 - conf, 4)
    tc = auxiliary.t_critico(n - 1, sig)
    left = media - tc * s / n ** 0.5
    right = media + tc * s / n ** 0.5
    res = {}
    res['left'] = str(left)
    res['right'] = str(right)
    return json.dumps(res, indent = 2)


def method_populacional(sucesso: float, total: float, conf: float):
    p = sucesso / total
    q = 1 - p
    zc = auxiliary.z_critico(round(conf/2, 4))
    aux = (p * q / total)**(0.5)
    left = p - zc * aux
    right = p + zc * aux
    res = {}
    res['left'] = str(left)
    res['right'] = str(right)
    return json.dumps(res, indent = 2)
