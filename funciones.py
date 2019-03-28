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


#nombrecarretera=doc.xpath('/RAIZ/PROVINCIA[NOMBRE="%s"]//CARRETERA/DENOMINACION/text()'%provincia)
#radarescarretera=doc.xpath('count(/RAIZ/PROVINCIA[NOMBRE="%s"]/CARRETERA//RADAR)'%provincia)
	


	#count(/RAIZ/PROVINCIA[NOMBRE="Albacete"]/CARRETERA[DENOMINACION="CM-3215"]//RADAR)