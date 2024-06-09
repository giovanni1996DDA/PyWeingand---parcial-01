from Domain.Libro import Libro


class LibroLocal(Libro):
    def __init__(self, codAfip, titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion):
        super().__init__(titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion)
        self.__CodAfip = codAfip

    def __str__(self):
        return f"Título:{self._Titulo} {self._Edicion}ª. edición, Autor: {self._Autor}, ISBN: {self._ISBN}, {self._Editorial}, Cod AFIP: {self.__CodAfip}, " \
               f"fecha {self._FecEdicion}, {self._CtdadPaginas} páginas"