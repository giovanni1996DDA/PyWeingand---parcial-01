from abc import ABCMeta, abstractmethod, ABC


class IGenericDao(metaclass=ABCMeta):
    @abstractmethod
    def save(self, libro):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, libro):
        pass