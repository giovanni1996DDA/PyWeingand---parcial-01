from DAO import LibroDao


class LibroBLL:

    def  __init__(self):
        pass

    @staticmethod
    def seleccionar():
        libroDao = LibroDao()
        return libroDao.get_all()

    @staticmethod
    def seleccionarByISBN(isbn):
        libroDao = LibroDao()
        return libroDao.getByISBN()

    @staticmethod
    def guardar(persona):
        libroDao = LibroDao()
        libroDao.guardar(persona)
        return persona

    @staticmethod
    def actualizar(persona):
        libroDao = LibroDao()
        libroDao.update(persona)