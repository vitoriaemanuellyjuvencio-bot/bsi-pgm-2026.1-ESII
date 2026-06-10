from abc import ABC, abstractmethod

class IRepositorioEmprestimo(ABC):

    @abstractmethod
    def buscar_equipamento(self, id):
        pass