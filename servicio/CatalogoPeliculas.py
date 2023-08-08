import os

class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listarPeliculas(cls):
        try:
            with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
                print('\n')
                print(' Catalogo '.center(50, '-'))
                print(archivo.read())
        except Exception as e:
            print(f'Archivo no encontrado: {e}')

    @classmethod
    def eliminarCatalogo(cls):
        try:
            os.remove(cls.ruta_archivo)
            print(f'Archivo eliminado: {cls.ruta_archivo}')
        except Exception as e:
            print(f'Archivo no encontrado: {e}')
