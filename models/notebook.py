from models.equipamento import Equipamento


class Notebook(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 10)