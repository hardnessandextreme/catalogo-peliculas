
# Catálogo de Películas

Este código representa un catálogo básico de películas implementado en Python, que permite agregar, listar y eliminar películas. Está dividido en tres componentes principales: la clase `Pelicula`, la clase `CatalogoPeliculas` y un archivo de prueba `test_catalogo_peliculas.py`.

## 1.   Pelicula.py (Clase Pelicula)
Esta clase define una película con su nombre. Proporciona una estructura simple para almacenar y mostrar el nombre de la película. Además, ofrece un método setter y getter para el nombre.
    
## 2.  CatalogoPeliculas.py (Clase CatalogoPeliculas)
La clase `CatalogoPeliculas` es responsable de gestionar el catálogo de películas. Contiene métodos estáticos para agregar, listar y eliminar películas. Las películas se almacenan en un archivo de texto llamado `peliculas.txt`. Los métodos disponibles son:
- `agregarPelicula(pelicula)`: Agrega una película al catálogo, guardando su nombre en el archivo.
- `listarPeliculas()`: Muestra en pantalla todas las películas en el catálogo.
- `eliminarCatalogo()`: Elimina el archivo de catálogo de películas.
    
## 3.  test_catalogo_peliculas.py 
Este archivo contiene un programa interactivo para probar las funcionalidades del catálogo. El usuario puede agregar películas, listarlas y eliminar el catálogo completo. El programa se ejecuta en un bucle hasta que el usuario decide salir.

![Menu](https://cdn.discordapp.com/attachments/1116592460009852971/1138577796478799981/image.png "Menu")
