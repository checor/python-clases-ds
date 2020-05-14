import csv
import datetime

def agrega_lugar():
    nombre = input("Inserte nombre del lugar: ")
    latitud = input("Inserte latitud: ")
    longitud = input("Inserte longitud: ")
    fecha_actual = datetime.datetime.now()
    with open("lugares.csv", "a") as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow([nombre, latitud, longitud, fecha_actual])


if __name__ == "__main__":
    cont = True
    while cont:
        agrega_lugar()
        c = input("Agregar otro lugar (s/N)? ")
        c = c.lower()
        if c.startswith("n") or c == "":
            cont = False
        elif c.startswith("s"):
            pass
        else:
            print("Comando no reconocido. Escriba si o no.")
        print("")

