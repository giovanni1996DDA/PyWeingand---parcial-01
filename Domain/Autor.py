class Autor:
    def __init__(self, nombre, apellido):
        self.__Nombre = nombre
        self.__Apellido = apellido

    def __str__(self):
        return(f"{self.__Nombre}, {self.__Apellido}")
