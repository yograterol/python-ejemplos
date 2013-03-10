"""
Ejemplo de Python-MongoEngine
"""

#Importamos los modulos de MongoEngine
from mongoengine import *


#Campos de los documentos de la coleccion Usuario
class Usuario(Document):
	correo = StringField(required=True)
	nombre = StringField(max_length=50)
	apellido = StringField(max_length=50)


def agregar_usuario(nombre, apellido, correo):
	"""
	Agrega un nuevo documento usuario
	a la coleccion Usuario
	"""
	print "Agregando al usuario con nombre: " , nombre
	usuario = Usuario()
	usuario.nombre = nombre
	usuario.apellido = apellido
	usuario.correo = correo
	
	if usuario.save():
		print "El usuario con nombre: " , nombre , \
			  " ha sido agregado.\n"


def borrar_usuario(nombre):
	"""
	Elimina un documento de la coleccion
	usuario
	"""
	usuario = Usuario.objects(nombre = nombre)[0]
	print "El usuario con nombre: " , usuario.nombre , " sera eliminado."
	usuario.delete()


def main():
	#Conexion al servidor
	#connect(BD, username='', password='')
	#Conecta al servidor local si no se le envia el parametro
	#host=''
	connect('prueba', username='prueba', password='prueba')

	#Agregando un usuario
	agregar_usuario("Yohan", "Graterol",
		            "yohangraterol92 (a r r o b a s i n s p a m) g m a i l dot com")

	#Busqueda e impresion de los usuarios en la coleccion
	for usuario in Usuario.objects:
		print "Nombre: " , usuario.nombre
		print "Apellido: " , usuario.apellido
		print "Correo: " , usuario.correo
		print

	#Se elimina el usuario
	borrar_usuario("Yohan")


if __name__ == "__main__":
	main()