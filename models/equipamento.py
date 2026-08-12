from abc import ABC, abstractmethod


class Equipamento(ABC):

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_multa(self, dias_atraso):
        pass