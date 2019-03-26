def nombresprovincias (doc):
	nombres = doc.xpath('RAIZ/PROVINCIA//NOMBRE/text()')
	return nombres