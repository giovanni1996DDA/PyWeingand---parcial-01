from abc import abstractmethod

from DAO.Interfaces.IGenericDao import IGenericDao


class LibroDAO(IGenericDao):
    lista_libros = []

    def __init__(self):
        pass

    def save(self, libro):
        LibroDAO.lista_libros.append(libro)

    def get_all(self):
        return LibroDAO.lista_libros

    def getByISBN(self, ISBN):
        for libro in LibroDAO.lista_libros:
            if libro.ISBN == ISBN:
                return libro
        return

    def update(self, libro):
        for i, n in enumerate(LibroDAO.lista_libros):
            if n.Titulo == libro.Titulo:
                LibroDAO.lista_libros[i] = libro
                return True
        return False
