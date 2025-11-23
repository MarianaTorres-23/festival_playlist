# festival_playlist
 Estás ayudando a organizar un gran festival de música donde se presentarán distintos artistas en varios escenarios. Para preparar el evento, necesitas crear una playlist inteligente que se adapte a los gustos del público.  Deberás trabajar con arreglos (listas) para almacenar canciones, duraciones y popularidad. Además, deberás generar reportes y permitir que el usuario interactúe con la playlist.

📌 Instrucciones
En Python, crea un programa llamado:
festival_playlist.py

El programa debe hacer lo siguiente:

🟩 A) Registrar canciones
Preguntar cuántas canciones desea agregar el usuario.

Por cada canción, pedir:

Nombre

Artista

Duración en minutos (float)

Popularidad (1–100)

Guarda cada dato en listas separadas, por ejemplo:

nombres = []
artistas = []
duraciones = []
popularidades = []

🟩 B) Generar reportes

El programa debe mostrar:

Número total de canciones

Duración total de la playlist

Canción más popular

Canción menos popular

Promedio de popularidad

🟩 C) Filtrar canciones
Permitir que el usuario busque canciones:

Por artista

Por un rango de popularidad

🟩 D) Bonus creativo
Generar una "playlist recomendada", incluyendo solo canciones con popularidad superior al promedio.

El programa debe tener un menú con las opciones:

1. Agregar canciones
2. Ver reportes
3. Buscar canciones
4. Playlist recomendada
5. Salir
