def curp(a_paterno, a_materno, nombre, fecha):
    ap = a_paterno[:2]
    am = a_materno[:1]
    n = nombre[:1]
    f = fecha[2:]
    print(ap + am + n + f)

curp("Limas", "Palma", "Amed", "19971202")
