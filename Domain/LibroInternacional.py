from Domain.Libro import Libro


class LibroInternacional(Libro):
    def __init__(self, paisorigen, titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion):
        super().__init__(titulo, autor, isbn, ctdadPaginas, edicion, editorial, fecedicion)
        self.__PaisOrigen = paisorigen

    def __str__(self):
        return f"Título:{self._Titulo} {self._Edicion}ª. edición, Autor: {self._Autor}, ISBN: {self._ISBN}, {self._Editorial}, {self.__PaisOrigen}, " \
               f"fecha {self._FecEdicion}, {self._CtdadPaginas} páginas"