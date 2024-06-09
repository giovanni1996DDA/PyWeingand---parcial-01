class BookNotFoundException(Exception):
    def __init__(self):
        super().__init__("No se encontro el libro")
