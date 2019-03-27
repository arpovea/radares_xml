from funciones import nombresprovincias
from funciones import numeroradares
from funciones import carreteraprovincia

from lxml import etree
doc = etree.parse('radares.xml')

while True:
	print ('''
	Elige una opcion:
	1-Muestra el nombre de las provincias de las que tenemos información sobre radares.
	2-Muestra la cantidad de radares de los que tenemos información.
	3-Pide por teclado una provincia, muestra el nombre de la carretera que tiene y la cantidad de radares.
	4-Pide por teclado una carretera, muestra el nombre de las provincias por las que pasa y sus radares.
	5-Pide por teclado una carretera, cuenta los radares que tiene y muestra las cordernadas de los radares.
	0-Para salir.
	''')
	opcion=int(input("Opcion: "))

	if opcion==1:
		for nombre in nombresprovincias(doc):
			print(nombre)
	elif opcion==2:
		print ("La cantidad de radares de los que tenemos inforcación es:", numeroradares(doc))
	elif opcion==3:
		provincia=str(input("Dime una provincia: "))
		for carretera in carreteraprovincia(provincia,doc):
			print ("Denominacion de carretera",carretera)