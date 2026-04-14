# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor
from temp_monitor import init
readings = input("Nombre del archivo: \n")

def main():
    nombre_archivo = input("Nombre del archivo.\n")
    nombree = nombre_archivo.strip().tittle()
    init(nombre_archivo)



if __name__ == "__main__":
    main()
