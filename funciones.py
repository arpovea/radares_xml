def nombresprovincias (doc):
	nombres = doc.xpath('/RAIZ/PROVINCIA//NOMBRE/text()')
	return nombres

def numeroradares (doc):
	numero = doc.xpath('count(/RAIZ/PROVINCIA/CARRETERA//RADAR)')
	return int(numero)

def carreteraprovincia(provincia,doc):
	listaradares=[]
	carretera = doc.xpath('/RAIZ/PROVINCIA[NOMBRE="%s"]//CARRETERA/DENOMINACION/text()'%provincia)
	for elem in carretera:
		radares = doc.xpath('count(/RAIZ/PROVINCIA[NOMBRE="%s"]/CARRETERA[DENOMINACION="%s"]//RADAR)'%(provincia,elem))
		listaradares.append(int(radares))
	return zip (carretera, listaradares)

def provinciacarretera(carretera,doc):
	listaradares=[]
	provincia=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)
	for elem in provincia:
		radares = doc.xpath('count(/RAIZ/PROVINCIA[NOMBRE="%s"]/CARRETERA[DENOMINACION="%s"]//RADAR)'%(elem,carretera))
		listaradares.append(int(radares))
	return zip (provincia, listaradares)

def cordenadasradares(carretera,doc):
	radares=int(doc.xpath('count(/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]//RADAR)'%carretera))
	
	provincia=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)
	for elem in provincia:

		print (elem)

		CordenadaInicial=[]
		CordenadaFinal=[]

		PuntoInicialLA=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)
		PuntoInicialLO=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)

		print(PuntoInicialLA)
		print(PuntoInicialLO)

		CordenadaInicial.append(PuntoInicialLA)
		CordenadaInicial.append(PuntoInicialLO)

		PuntoFinalLA=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_FINAL/LATITUD/text()'%carretera)
		PuntoFinalLO=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_FINAL/LONGITUD/text()'%carretera)

		CordenadaFinal.append(PuntoFinalLA)
		CordenadaFinal.append(PuntoFinalLO)

	print (CordenadaInicial)
	print (CordenadaFinal)

	return  radares, CordenadaInicial, CordenadaFinal