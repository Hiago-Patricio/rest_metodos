from flask import Flask, request
import json
# metodos
import function_zeros, interpolation


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

if __name__ == '__main__':
	app.run()