nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    print("\nAgregar canciones")
    cantidad = int(input("¿Cuántas canciones deseas agregar? "))

    for i in range(cantidad):
        print(f"\nCanción {i+1}:")
        nombre = input("Nombre: ")
        artista = input("Artista: ")
        duracion = float(input("Duración (minutos): "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\nCanciones agregadas correctamente.\n")


def ver_reportes():
    print("\nReportes")

    if len(nombres) == 0:
        print("No hay canciones registradas.\n")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)

    indice_max = popularidades.index(max(popularidades))
    cancion_max = nombres[indice_max]
    artista_max = artistas[indice_max]

    indice_min = popularidades.index(min(popularidades))
    cancion_min = nombres[indice_min]
    artista_min = artistas[indice_min]

    promedio = sum(popularidades) / total

    print(f"Total de canciones: {total}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {cancion_max} - {artista_max}")
    print(f"Canción menos popular: {cancion_min} - {artista_min}")
    print(f"Promedio de popularidad: {promedio:.2f}\n")


def buscar_canciones():
    print("\nBuscar canciones")
    if len(nombres) == 0:
        print("No hay canciones registradas.\n")
        return

    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        artista_buscar = input("Ingresa el nombre del artista: ")
        print("\nResultados:")

        encontrado = False
        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar.lower():
                print(f"- {nombres[i]} (Popularidad: {popularidades[i]})")
                encontrado = True

        if not encontrado:
            print("No se encontraron canciones de ese artista.")

    elif opcion == "2":
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))
        print("\nResultados:")

        encontrado = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"- {nombres[i]} - {artistas[i]} (Popularidad: {popularidades[i]})")
                encontrado = True

        if not encontrado:
            print("No hay canciones dentro de ese rango.")

    print()


def playlist_recomendada():
    print("\nPlaylist Recomendada")
    if len(nombres) == 0:
        print("No hay canciones registradas.\n")
        return

    promedio = sum(popularidades) / len(popularidades)
    print(f"Popularidad promedio: {promedio:.2f}")
    print("Canciones recomendadas:\n")

    encontrado = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"- {nombres[i]} - {artistas[i]} (Popularidad: {popularidades[i]})")
            encontrado = True

    if not encontrado:
        print("No hay canciones con popularidad superior al promedio.\n")
    print()


def menu():
    while True:
        print("FESTIVAL PLAYLIST")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print("\nPrograma finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

menu()
