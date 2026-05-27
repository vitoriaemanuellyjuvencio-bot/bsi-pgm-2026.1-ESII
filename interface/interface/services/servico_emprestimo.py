# Responsabilidade: gerenciar regras de empréstimos

from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador

class ServicoEmprestimo:
    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, usuario, equipamento):
        emprestimo = {
            "usuario": usuario,
            "equipamento": equipamento
        }
        self.repo.salvar_emprestimo(emprestimo)
        self.notificador.enviar("Empréstimo realizado")

    def listar(self):
        for e in self.repo.listar_emprestimos():
            print(e)
    

    def calcular_multa(self, equipamento, dias_atraso):
        return
    equipamento.calcular_multa(dias_atraso) # type: ignore