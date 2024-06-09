import random

from BLL.Exceptions.BookNotFoundException import BookNotFoundException
from BLL.LibroBLL import LibroBLL
from Domain.Autor import Autor
from Domain.LibroInternacional import LibroInternacional
from Domain.LibroLocal import *


class program:
    def __init__(self):
        pass

    @staticmethod
    def run():
        tolkien = Autor(nombre="J.R.R.",
                        apellido="Tolkien")
        silmarillion = LibroInternacional(paisorigen="Reino Unido",
                                          titulo="El silmarillion",
                                          autor=tolkien,
                                          isbn="9780618391110",
                                          ctdadPaginas=552,
                                          edicion=2,
                                          editorial="Minotauro",
                                          fecedicion="01/04/2023")
        print(silmarillion)
        print()
        print(silmarillion.getCategoria())
        print()

        martinez = Autor(nombre="Tomás Eloy",
                         apellido="Martinez")
        santatevita = LibroLocal(codAfip=random.randint(1000, 9999),
                                 titulo="Santa Evita",
                                 autor=martinez,
                                 isbn="978-987-738-714-8",
                                 ctdadPaginas=348,
                                 edicion=2,
                                 editorial="Alfaguara",
                                 fecedicion="08/12/2020")

        print(santatevita)
        print()
        print(santatevita.getCategoria())
        print()

        rowling = Autor(nombre="J.K.",
                        apellido="Rowling")
        

        LibroBLL.save(LibroInternacional(paisorigen="Reino Unido",
                                         titulo="Harry Potter",
                                         autor=rowling,
                                         isbn="9788498382662",
                                         ctdadPaginas=256,
                                         edicion=1,
                                         editorial="Magia 2.0",
                                         fecedicion="03/06/2010"))

        try:
            harrypotter = LibroBLL.getByISBN("97884983asd82662")

            print(harrypotter)
            print()
            print(harrypotter.getCategoria())
            print()
        except BookNotFoundException as ex:
            print(ex)
        





program.run()
