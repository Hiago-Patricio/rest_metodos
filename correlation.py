import auxiliary


def start_pearson(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_pearson(x, y)


def start_spearman(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_spearman(x, y)


def start_kendall(x, y):
    x = auxiliary.str_list(x)
    x = auxiliary.list_float(x)
    y = auxiliary.str_list(y)
    y = auxiliary.list_float(y)
    return method_kendall(x, y)


def method_pearson(x: list, y: list):
    media_x = sum(x) / len(x)
    media_y = sum(y) / len(y)

    somatorio1 = 0
    somatorio2 = 0
    somatorio3 = 0
    for i, j in zip(x, y):
        somatorio1 += (i - media_x) * (j - media_y)
        somatorio2 += (i - media_x) ** 2
        somatorio3 += (j - media_y) ** 2
    r = somatorio1 / (somatorio2**(0.5) * somatorio3**(0.5))
    return auxiliary.convert_json('r', r)


def method_spearman(x: list, y: list):
    x_sorted = sorted(x)
    y_sorted = sorted(y)
    n = len(x)
    somatorio = 0
    for i,j in zip(x, y):
        first_x = int(auxiliary.position(i, x_sorted))
        last_x = first_x + int(auxiliary.repetead_amount(i, x_sorted))
        x_equals = auxiliary.repetead_amount(i, x_sorted)

        first_y = int(auxiliary.position(j, y_sorted))
        last_y = first_y + int(auxiliary.repetead_amount(j, y_sorted))
        y_equals = auxiliary.repetead_amount(j, y_sorted)

        pos_x = sum(range(first_x, last_x)) / x_equals
        pos_y = sum(range(first_y, last_y)) / y_equals

        d = pos_x - pos_y
        somatorio += d ** 2
    p = 1 - 6 * somatorio / (n * (n ** 2 - 1))
    return auxiliary.convert_json('p', p)


def method_kendall(x: list, y:list):
    concordant = 0
    discordant = 0
    n = len(x)
    for i in range(n-1):
        for j in range(i+1, n):
            if x[j] > x[i] and y[j] > y[i] or x[j] < x[i] and y[j] < y[i]:
                concordant += 1
            else:
                discordant += 1
    r = (concordant - discordant) / (n*(n-1)/2)
    return auxiliary.convert_json('r', r)