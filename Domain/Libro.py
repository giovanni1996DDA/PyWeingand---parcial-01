from abc import ABC


class Libro(ABC):

    def __init__(self, titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion):
        self._Titulo = titulo
        self._Autor = autor
        self._ISBN = isbn
        self._CtdadPaginas = ctdadPaginas
        self._Edicion = edicion
        self._Editorial = editorial
        self._FecEdicion = fecedicion

    def getCategoria(self):
        if self._CtdadPaginas <= 0:
            return "Libro sin establecer"
        if self._CtdadPaginas < 200:
            return "Libro corto"
        if self._CtdadPaginas < 500:
            return "Libro convencional"
        return "Libro extenso"

    def getTitulo(self):
        return self._Titulo

    def getISBN(self):
        return self._ISBN

    Titulo = property(getTitulo)
    ISBN = property(getISBN)
    Categoria = property(getCategoria)
