from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

loop = True
choice = None

def crearPelicula():
    nombrePelicula = input('Ingrese el nombre de la pelicula: ')
    pelicula = Pelicula(nombre=nombrePelicula)
    return pelicula


while loop:
    print('1. Agregar Pelicula\n'
          '2. Listar peliculas\n'
          '3. Eliminar catalogo de peliculas\n'
          '4. Salir')

    try:
        choice = int(input('Ingrese una opcion: '))

        if choice == 1:
            pelicula = crearPelicula()
            CatalogoPeliculas.agregarPelicula(pelicula)

        elif choice == 2:
            CatalogoPeliculas.listarPeliculas()

        elif choice == 3:
            CatalogoPeliculas.eliminarCatalogo()

        elif choice == 4:
            print('Adios')
            loop = False

        else:
            print('Ingrese una opcion valida.')

    except KeyboardInterrupt:
        print(f'\nFinalizado por interrupcion de teclas')
        loop = False

    except Exception as e:
        print(f'Error: {e}')