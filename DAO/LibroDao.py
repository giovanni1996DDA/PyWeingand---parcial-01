from Interfaces import IGenericDao


class LibroDao(IGenericDao):
    lista_libros = []

    def guardar(self, libro):
        LibroDao.lista_libros.append(libro)

    def get_all(self):
        return LibroDao.lista_libros

    def getByISBN(self, ISBN):
        for libro in LibroDao.lista_libros:
            if libro.ISBN == ISBN:
                return libro

    def update(self, libro):
        for n in LibroDao.lista_libros:
            if n.Titulo == libro.Titulo:
                n = libro
