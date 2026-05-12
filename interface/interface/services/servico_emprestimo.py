# Responsabilidade: gerenciar regras de empréstimos

from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador

class ServicoEmprestimo:
    def __init__(self):
        self.repo = RepositorioEmprestimo()
        self.notificador = Notificador()

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