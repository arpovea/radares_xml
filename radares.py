from funciones import *
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
		print("La cantidad de radares de los que tenemos inforcación es:", numeroradares(doc))
	elif opcion==3:
		provincia=str(input("Dime una provincia: "))
		for carretera,radares in carreteraprovincia(provincia,doc):
			print ("Carretera:",carretera,"-->","Radares:",radares)
	elif opcion==4:
		carretera=str(input("Dime una carretera: "))
		for provincia,radares in provinciacarretera(carretera,doc):
			print ("Pasa por la provincia de:", provincia,"y tiene", radares, "radares.")
	elif opcion==5:
		carretera=str(input("Dime una carretera: "))
		radar=1
		for LATITUD,LONGUITUD in cordenadasradares(carretera,doc):
			for elem,elem1 in zip(LATITUD,LONGUITUD):
				print ("Radar:",radar)
				print ("Latitud:",elem,"Longitud:",elem1)
				print("Enlace openstreetmap:",end=" ")
				print(f"http://www.openstreetmap.org/#map=15/{elem}/{elem1}")
				radar=radar+1
	elif opcion==0:
		print("Hasta la proxima!")
		break;