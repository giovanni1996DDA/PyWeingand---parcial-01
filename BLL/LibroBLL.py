from BLL.Exceptions.BookNotFoundException import BookNotFoundException
from DAO.LibroDAO import LibroDAO


class LibroBLL:

    def __init__(self):
        pass

    @staticmethod
    def getAll():
        libroDao = LibroDAO()
        return libroDao.get_all()

    @staticmethod
    def getByISBN(isbn):
        libroDao = LibroDAO()
        res = libroDao.getByISBN(isbn)
        if res == None:
            raise BookNotFoundException()
        return res

    @staticmethod
    def save(libro):
        libroDao = LibroDAO()
        libroDao.save(libro)
        return libro

    @staticmethod
    def update(libro):
        libroDao = LibroDAO()
        updated = libroDao.update(libro)
        if not updated:
            raise BookNotFoundException()