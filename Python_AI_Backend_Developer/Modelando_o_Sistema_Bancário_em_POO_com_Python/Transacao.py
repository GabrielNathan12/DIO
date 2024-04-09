from abc import ABC, abstractmethod
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registar(self, conta):
        pass