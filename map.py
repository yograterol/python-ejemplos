'''
Codigo de ejemplo sobre Map y Reduce
'''
from time import clock

def div(x):
	'''
	Devuelve la division de x + 1con x
	'''
	return (x + 1)/x 

def suma(x,y):
	'''
	Devuelve la suma de X con Y
	'''
	return x + y

if __name__ == "__main__":
	# Lista o Tuplas de numeros a tratar
	sec = range(1, 500001)

	sec_1 = list()

	######## DIVISION CON UN FOR ########
	start_for = clock()
	for i in sec:
		sec_1.append((i + 1)/i)
	end_for = clock()

	######## DIVISION CON MAP ########
	# Map aplicada con una funcion definida y con lambda
	start_map1 = clock()
	map1 = map(div, sec)
	end_map1 = clock()

	######## SUMA CON REDUCE ########
	start_map2 = clock()
	map2 = map(lambda x: (x + 1)/x, sec)
	end_map2 = clock()


	# Reduce aplicada con una funcion definida y con lambda
	reduce1 = reduce(suma, sec)
	reduce2 = reduce(lambda x, y: x + y, sec)

	print "Division con un for (", end_for - start_for ," s)"
	print "Division con Map y funcion definida (", end_map1 - start_map1 ," s)"
	print "Division con Map y funcion lambda (", end_map2 - start_map2 ," s)"
