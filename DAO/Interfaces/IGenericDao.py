from abc import ABCMeta, abstractmethod


class IGenericDao(metaclass=ABCMeta):

    @abstractmethod
    def guardar(self, Persona):
        pass

    @abstractmethod
    def get_all(self):
        pass