def nombresprovincias (doc):
	nombres = doc.xpath('/RAIZ/PROVINCIA//NOMBRE/text()')
	return nombres

def numeroradares (doc):
	numero = doc.xpath('count(/RAIZ/PROVINCIA/CARRETERA//RADAR)')
	return int(numero)
def carreteraprovincia(provincia,doc):
	nombrecarretera=doc.xpath('/RAIZ/PROVINCIA[NOMBRE="%s"]//CARRETERA/DENOMINACION/text()'%provincia)
	radarescarretera=doc.xpath('count(/RAIZ/PROVINCIA[NOMBRE="%s"]/CARRETERA//RADAR)'%provincia)
	return nombrecarretera,radarescarretera

	