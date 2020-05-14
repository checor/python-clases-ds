cont  = True

while cont:
    nombre = input("Inserte nombre del lugar: ")
    latitud = input("Inserte latitud: ")
    longitud = input("Inserte longitud: ")
    with open("hoteles.txt", 'a') as estaciones_file:
        estaciones_file.write("{}\t{}\t{}\n".format(nombre, latitud, longitud))
    valid = False
    while not valid:
        c = input("Agregar otro lugar? (s/N)? ")
        c = c.lower()
        if c.startswith('s'):
            cont = True
            valid = True
        elif c.startswith('n'):
            cont = False
            valid = True
        else:
            print("Respuesta no válida")
            valid = False
    print("")
