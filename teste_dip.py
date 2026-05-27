from services.servico_emprestimo import ServicoEmprestimo
from models.notebook import Notebook

class RepositorioFalso:
    def __init__(self):
        self.emprestimos = []

    def salvar(self, emprestimo):
        self.emprestimos.append(emprestimo)


class NotificadorFalso:
    def __init__(self):
        self.notificacoes = []

    def notificar_emprestimo(self, mensagem):
        self.notificacoes.append(mensagem)

    def notificar_devolucao(self, mensagem):
        self.notificacoes.append(mensagem)

    def notificar_atraso(self, mensagem):
        self.notificacoes.append(mensagem)

repositorio = RepositorioFalso()
notificador = NotificadorFalso()

servico = ServicoEmprestimo(repositorio, notificador)

equipamento = Notebook("Dell")

servico.registrar("Vitória", equipamento, 5)

print(repositorio.emprestimos)
print(notificador.notificacoes)



