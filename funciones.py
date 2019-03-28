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
	listaradares=[]
	radares=int(doc.xpath('count(/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]//RADAR)'%carretera))
	listaradares.append(radares)
	provincia=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)
	for var in range (0,radares):
		CordenadasIniciales=[]
		PuntoInicialLA=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)
		PuntoInicialLO=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)
		#print(PuntoInicialLA)
		#print(PuntoInicialLO)
		CordenadasIniciales.append(PuntoInicialLA)
		CordenadasIniciales.append(PuntoInicialLO)
		#print (CordenadaInicial[0])
		#print (CordenadaInicial[1])
		print ("Radares:", listaradares[0],"Latitud:",CordenadasIniciales[0],"Longitud:",CordenadasIniciales[1])
	

	#print (listaradares)
	#print (CordenadaInicial)



def cordenadasradaressss(carretera,doc):
	listaradares=[]
	CordenadaInicial=[]
	
	radares=int(doc.xpath('count(/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]//RADAR)'%carretera))
	listaradares.append(radares)
	
	#provincia=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)
	
	for var in range (0,radares):

		#print (elem)

		PuntoInicialLA=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)
		PuntoInicialLO=doc.xpath('/RAIZ/PROVINCIA/CARRETERA[DENOMINACION ="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)

		print(PuntoInicialLA)
		print(PuntoInicialLO)

		CordenadaInicial.append(PuntoInicialLA)
		CordenadaInicial.append(PuntoInicialLO)

	return zip (listaradares, CordenadaInicial)


	#print (listaradares)
	#print (CordenadaInicial)
