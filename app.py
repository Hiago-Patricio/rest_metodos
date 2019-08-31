from flask import Flask, request
import json
# metodos
import correlation
import function_zeros, interpolation
import intervals
import regression

app = Flask(__name__)


'''
Funções esperadas, sendo x em radianos nas funções 2, 3 e 4:
1 - log(x)
2 - ln(x)
3 - cos(x)
4 - sen(x)
5 - tan(x)
6 - sec(x)
7 - csc(x)
8 - cot(x)
Constantes esperadas:
1 - pi
2 - e
Modificador de precedência:
1 - ()
Operadores esperados, a precedência das operações é como na matemática:
1 - ^
2 - *
3 - /
4 - +
5 - -
Exemplos de funções aceitas:
1 - log(x) - x + 2
2 - e^x - x - 5
3 - cos(x) - x
4 - x^3 - 5 * x + 2
5 - 2 / (x + 5)
'''


'''
Exemplo de input esperado:
{
	"a": "3", 
	"b": "2",
	"error": "0.01",
	"function": "log(x) - x + 2" 
}
'''
@app.route('/bisection', methods=['POST'])
def f_bisection():
	a = request.json['a']
	b = request.json['b']
	error = request.json['error']
	function = request.json['function']
	return function_zeros.start_bisection(a, b, error, function)


'''
Exemplo de input esperado:
{
	"a": "3", 
	"b": "2",
	"error": "0.01",
	"function": "log(x) - x + 2" 
}
'''
@app.route('/false_position', methods=['POST'])
def f_false_position():
	a = request.json['a']
	b = request.json['b']
	error = request.json['error']
	function = request.json['function']
	return function_zeros.start_false_position(a, b, error, function)


'''
Exemplo de input esperado:
{
	"x": "3", 
	"error": "0.01",
	"function": "log(x) - x + 2", 
	"derivative": "1/x/ln(10)-1"
}
'''
@app.route('/newton_raphson', methods=['POST'])
def f_newton_raphson():
	x = request.json['x']
	error = request.json['error']
	function = request.json['function']
	derivative_function = request.json['derivative']
	return function_zeros.start_newton_raphson(x, error, function, derivative_function)


'''
Exemplo de input esperado:
{
	"x0": "3", 
	"x1": "2",
	"error": "0.01",
	"function": "log(x) - x + 2" 
}
'''
@app.route('/secant', methods=['POST'])
def f_secant():
	x0 = request.json['x0']
	x1 = request.json['x1']
	error = request.json['error']
	function = request.json['function']
	return function_zeros.start_secant(x0, x1, error, function)


'''
Exemplo de input esperado:
{
	"x": "3, 5, 7, 8",
	"y": "1, 9, 0, 11"
}
'''
@app.route('/lagrange', methods=['POST'])
def f_lagrange():
	x = request.json['x']
	y = request.json['y']
	return interpolation.start_lagrange(x, y)


'''
Exemplo de input esperado:
{
	"x": "3, 5, 7, 8",
	"d0": "1, 9, 0, 11"
}
'''
@app.route('/newton_polynomial', methods=['POST'])
def f_newton_polynomial():
	x = request.json['x']
	d0 = request.json['d0']
	return interpolation.start_newton_polynomial(x, d0)


'''
Exemplo de input esperado:
{
	"x": "0,1,2,3",
	"y": "1,3,-2,1"
}
'''
@app.route('/trigonometric', methods=['POST'])
def f_trigonometic():
	x = request.json['x']
	y = request.json['y']
	return interpolation.start_trigonometric(x, y)

'''
Exemplo de input esperado:
{
	"x": "3, 5, 7, 8",
	"y": "1, 9, 0, 11"
}
'''
@app.route('/spline', methods=['POST'])
def f_spline():
	x = request.json['x']
	y = request.json['y']
	return interpolation.start_spline(x, y)


'''
Exemplo de input esperado:
{
	"x": "3, 5, 7, 8",
	"y": "1, 9, 0, 11"
}
'''
@app.route('/pearson', methods=['POST'])
def f_pearson():
	x = request.json['x']
	y = request.json['y']
	return correlation.start_pearson(x, y)


'''
Exemplo de input esperado:
{
	"x": "86,97,99,100,101,103,106,110,112,113",
	"y": "0,20,28,27,50,29,7,17,6,12"
}
'''
@app.route('/spearman', methods=['POST'])
def f_spearman():
	x = request.json['x']
	y = request.json['y']
	return correlation.start_spearman(x, y)


'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5",
	"y": "7,5,1,6,9"
}
'''
@app.route('/kendall', methods=['POST'])
def f_kendall():
	x = request.json['x']
	y = request.json['y']
	return correlation.start_kendall(x, y)


'''
Exemplo de input esperado:
{
	"y": "139,126,90,144,163,136,61,62,41,120",
	"x": "122,114,86,134,146,107,68,117,71,98"
}
'''
@app.route('/linear', methods=['POST'])
def f_linear():
	x = request.json['x']
	y = request.json['y']
	return regression.start_linear(x, y)


'''
dpp = Desvio padrao populacional
n = Tamanho da amostra
conf = Confiança
Exemplo de input esperado:
{
	"dpp": "5",
	"n": "100",
	"media": "500", 
	"conf": "0.475" 
}
'''
@app.route('/normal', methods=['POST'])
def f_interval_normal():
	dpp = request.json['dpp']
	n = request.json['n']
	media = request.json['media']
	conf = request.json['conf']
	return intervals.start_normal(dpp, n, media, conf)


'''
conf = Confiança
Exemplo de input esperado:
{
    "amostra": "9, 8, 12, 7, 9, 6, 11, 6, 10, 9",
    "conf": "0.95"
}
'''
@app.route('/student', methods=['POST'])
def f_t_student():
    amostra = request.json['amostra']
    conf = request.json['conf']
    return intervals.start_t_student(amostra, conf)


'''
conf = Confiança
Exemplo de input esperado:
{
    "sucesso": "160",
    "total": "200",
    "conf": "0.95"
}
'''
@app.route('/populacional', methods=['POST'])
def f_populacional():
    sucesso = request.json['sucesso']
    total = request.json['total']
    conf = request.json['conf']
    return intervals.start_populacional(sucesso, total, conf)


'''
Bootstrap
Exemplo de input esperado:
	"amostra": "2.2, 2.5, 3.4, 6.7, 6.2, 8.2, 9.2, 7.9, 9.2, 10.1"
'''


'''
Exemplo de input esperado:
	"populacao": 
'''



'''
Exemplo de input esperado:
{
    "dpp": 
    "n": 
    "media": 
    
}
'''



if __name__ == '__main__':
	app.run()