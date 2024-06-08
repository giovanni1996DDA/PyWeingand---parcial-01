from Domain.Libro import Libro


class LibroLocal(Libro):
    def __init__(self, cofAfip, titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion):
        super().__init__(titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion)
        self.__CodAfip = cofAfip

    def __str__(self):
        return f"Título:{self._Titulo} {self._Edicion}a. edición, Autor: {self._Autor}, ISBN: {self._ISBN}, {self._Editorial}, {self._CodAfip}, " \
               f"fecha {self._fecEdicion}, {self.__CtdadPaginas} páginas"